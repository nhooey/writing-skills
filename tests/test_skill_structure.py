import unittest

from skill_structure import parse_frontmatter, relative_links, skill_problems

GOOD_MD = """---
name: demo-skill
description: Does one thing well.
---

# Demo

See [the examples](examples.md) and [the spec](https://example.com/spec).
"""

GOOD_FLAKE = """{
  outputs = { agent-skill-flake, ... }:
    agent-skill-flake.lib.mkSkillFlake {
      skillName = "demo-skill";
      src = ./.;
    };
}
"""

FILES = {"SKILL.md", "flake.nix", "examples.md"}


def problems(md=GOOD_MD, flake=GOOD_FLAKE, files=FILES, dir_name="demo-skill"):
    return skill_problems(dir_name, md, flake, files)


class ParseFrontmatterTest(unittest.TestCase):
    def test_reads_plain_and_quoted_values(self):
        fields = parse_frontmatter(
            '---\nname: a-b\ndescription: "Quoted: yes"\n---\nbody\n'
        )
        self.assertEqual(fields, {"name": "a-b", "description": "Quoted: yes"})

    def test_joins_a_folded_block_scalar(self):
        fields = parse_frontmatter(
            "---\nname: a\ndescription: >\n  first line\n  second line\n---\n"
        )
        self.assertEqual(fields["description"], "first line second line")

    def test_none_without_an_opening_fence(self):
        self.assertIsNone(parse_frontmatter("name: a\n---\n"))

    def test_none_without_a_closing_fence(self):
        self.assertIsNone(parse_frontmatter("---\nname: a\n"))


class RelativeLinksTest(unittest.TestCase):
    def test_keeps_local_targets_and_drops_urls_and_anchors(self):
        text = "[a](a.md) [b](https://x.org) [c](#top) [d](./refs/d.md#part) [e](mailto:x@y)\n"
        self.assertEqual(relative_links(text), ["a.md", "refs/d.md"])

    def test_ignores_links_inside_code_fences_and_spans(self):
        text = "```markdown\n[x](missing.md)\n```\n`[y](also-missing.md)`\n[z](z.md)\n"
        self.assertEqual(relative_links(text), ["z.md"])


class SkillProblemsTest(unittest.TestCase):
    def test_well_formed_skill_has_no_problems(self):
        self.assertEqual(problems(), [])

    def test_missing_skill_md(self):
        self.assertEqual(problems(md=None), ["SKILL.md is missing"])

    def test_missing_frontmatter(self):
        found = problems(md="# Demo\n")
        self.assertIn("SKILL.md has no frontmatter block", found)
        self.assertIn("frontmatter description is missing or empty", found)

    def test_name_differs_from_directory(self):
        found = problems(md=GOOD_MD.replace("name: demo-skill", "name: other-skill"))
        self.assertEqual(
            found,
            ["frontmatter name 'other-skill' does not match directory 'demo-skill'"],
        )

    def test_directory_name_not_kebab_case(self):
        md = GOOD_MD.replace("demo-skill", "Demo_Skill")
        flake = GOOD_FLAKE.replace("demo-skill", "Demo_Skill")
        found = problems(md=md, flake=flake, dir_name="Demo_Skill")
        self.assertEqual(len(found), 1)
        self.assertIn("is not lowercase words joined by hyphens", found[0])

    def test_directory_name_too_long(self):
        long_name = "a" * 65
        md = GOOD_MD.replace("demo-skill", long_name)
        flake = GOOD_FLAKE.replace("demo-skill", long_name)
        self.assertEqual(len(problems(md=md, flake=flake, dir_name=long_name)), 1)

    def test_empty_description(self):
        found = problems(md=GOOD_MD.replace("Does one thing well.", ""))
        self.assertEqual(found, ["frontmatter description is missing or empty"])

    def test_description_at_the_limit_passes_and_over_it_fails(self):
        at_limit = GOOD_MD.replace("Does one thing well.", "x" * 1024)
        over = GOOD_MD.replace("Does one thing well.", "x" * 1025)
        self.assertEqual(problems(md=at_limit), [])
        self.assertEqual(
            problems(md=over),
            ["frontmatter description is 1025 characters, over the 1024 limit"],
        )

    def test_missing_flake(self):
        self.assertEqual(problems(flake=None), ["flake.nix is missing"])

    def test_flake_builds_a_different_skill_name(self):
        found = problems(flake=GOOD_FLAKE.replace('"demo-skill"', '"demo-skil"'))
        self.assertEqual(
            found, ["flake.nix skillName ['demo-skil'] does not match 'demo-skill'"]
        )

    def test_broken_relative_link(self):
        found = problems(files={"SKILL.md", "flake.nix"})
        self.assertEqual(
            found, ["SKILL.md links to 'examples.md', which does not exist"]
        )


if __name__ == "__main__":
    unittest.main()
