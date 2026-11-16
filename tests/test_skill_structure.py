import contextlib
import io
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from skill_structure import (
    build_parser,
    check,
    default_skills_dir,
    main,
    parse_frontmatter,
    relative_links,
    skill_problems,
)

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

    def test_joins_a_plain_value_continued_on_indented_lines(self):
        fields = parse_frontmatter(
            "---\nname: a\ndescription: first part\n  continued here\n---\n"
        )
        self.assertEqual(fields["description"], "first part continued here")

    def test_joins_a_quoted_value_continued_on_indented_lines(self):
        fields = parse_frontmatter(
            '---\nname: a\ndescription: "Quoted: first\n  then more"\n---\n'
        )
        self.assertEqual(fields["description"], "Quoted: first then more")

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

    def test_a_shorter_fence_inside_a_longer_one_does_not_close_it(self):
        text = "````markdown\n```\n[x](missing.md)\n```\n````\n[y](y.md)\n"
        self.assertEqual(relative_links(text), ["y.md"])

    def test_keeps_local_reference_definitions(self):
        text = "See [a][ref].\n\n[ref]: refs/a.md\n[web]: https://x.org\n"
        self.assertEqual(relative_links(text), ["refs/a.md"])


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

    def test_over_long_description_wrapped_over_lines_fails(self):
        wrapped = "\n  ".join(["x" * 100] * 11)
        found = problems(md=GOOD_MD.replace("Does one thing well.", wrapped))
        self.assertEqual(
            found,
            ["frontmatter description is 1110 characters, over the 1024 limit"],
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


class ParserTest(unittest.TestCase):
    def parse(self, *argv):
        with contextlib.redirect_stderr(io.StringIO()):
            return build_parser().parse_args(list(argv))

    def test_check_takes_an_optional_skills_dir(self):
        self.assertIsNone(self.parse("check").skills_dir)
        self.assertEqual(self.parse("check", "elsewhere").skills_dir, Path("elsewhere"))

    def test_a_command_is_required(self):
        with self.assertRaises(SystemExit) as raised:
            self.parse()
        self.assertEqual(raised.exception.code, 2)

    def test_unknown_command_is_rejected(self):
        with self.assertRaises(SystemExit) as raised:
            self.parse("lint")
        self.assertEqual(raised.exception.code, 2)

    def test_help_lists_the_check_command(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit):
            build_parser().parse_args(["--help"])
        self.assertIn("check", out.getvalue())

    def test_default_skills_dir_follows_prj_root(self):
        with mock.patch.dict(os.environ, {"PRJ_ROOT": "/repo"}):
            self.assertEqual(default_skills_dir(), Path("/repo/skills"))
        with mock.patch.dict(os.environ, clear=True):
            self.assertEqual(default_skills_dir(), Path("skills"))


class CheckTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)

    def write_skill(self, name, md=GOOD_MD, flake=GOOD_FLAKE):
        skill = self.tmp / name
        skill.mkdir()
        (skill / "SKILL.md").write_text(md)
        (skill / "flake.nix").write_text(flake)
        (skill / "examples.md").write_text("")

    def run_check(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = main(["check", *argv])
        return status, out.getvalue(), err.getvalue()

    def test_well_formed_skills_pass(self):
        self.write_skill("demo-skill")
        status, out, err = self.run_check(str(self.tmp))
        self.assertEqual((status, out, err), (0, "1 skills well formed\n", ""))

    def test_a_malformed_skill_fails_and_names_itself(self):
        self.write_skill("demo-skill")
        self.write_skill("other-skill")
        status, _, err = self.run_check(str(self.tmp))
        self.assertEqual(status, 1)
        self.assertIn("other-skill: frontmatter name", err)
        self.assertNotIn("demo-skill:", err)

    def test_empty_skills_dir_fails(self):
        self.assertEqual(self.run_check(str(self.tmp))[0], 1)

    def test_missing_skills_dir_is_a_usage_error(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(check(self.tmp / "absent"), 2)


if __name__ == "__main__":
    unittest.main()
