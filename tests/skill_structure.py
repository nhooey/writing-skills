"""Check that every skill under a skills directory is well formed.

For each `skills/<dir>/`:

- `SKILL.md` opens with a frontmatter block.
- The frontmatter `name` equals `<dir>` and is a valid skill name.
- The frontmatter `description` is present and within the length limit.
- The skill's `flake.nix` builds it under the same `skillName`.
- Every relative link in `SKILL.md` outside a code fence names a file
  that exists in the skill directory.

Run as `skill-structure check [SKILLS_DIR]` from the dev shell; see
`skill-structure --help`.
"""

import argparse
import os
import posixpath
import re
import sys
from pathlib import Path

NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NAME_MAX = 64
DESCRIPTION_MAX = 1024
LINK_PATTERN = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKILL_NAME_IN_FLAKE = re.compile(r'skillName\s*=\s*"([^"]*)"\s*;')
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")


def parse_frontmatter(text):
    """Return the frontmatter's top-level keys as a dict, or None.

    Understands the subset skills use: `key: value` lines, quoted values,
    and block scalars (`>`, `|`) whose lines are indented under the key.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return None
    fields = {}
    key = None
    block = False
    for line in lines[1:end]:
        if block and (line.startswith((" ", "\t")) or not line.strip()):
            fields[key] = (fields[key] + " " + line.strip()).strip()
            continue
        block = False
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip()
        if value in (">", "|", ">-", "|-", ""):
            fields[key] = ""
            block = True
        else:
            fields[key] = unquote(value)
    return fields


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def relative_links(text):
    """Return the link targets outside code fences that point at local files."""
    targets = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_PATTERN.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = re.sub(r"`[^`]*`", "", line)
        for target in LINK_PATTERN.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if path:
                targets.append(posixpath.normpath(path))
    return targets


def skill_problems(dir_name, skill_md, flake_nix, existing_files):
    """Return a list of problems with one skill; empty means well formed.

    `skill_md` and `flake_nix` are file contents (None if the file is
    missing); `existing_files` is the set of paths, relative to the skill
    directory, that exist in it.
    """
    if skill_md is None:
        return ["SKILL.md is missing"]
    problems = []
    fields = parse_frontmatter(skill_md)
    if fields is None:
        problems.append("SKILL.md has no frontmatter block")
        fields = {}
    name = fields.get("name", "")
    if name != dir_name:
        problems.append(
            f"frontmatter name {name!r} does not match directory {dir_name!r}"
        )
    if not NAME_PATTERN.match(dir_name) or len(dir_name) > NAME_MAX:
        problems.append(
            f"directory name {dir_name!r} is not lowercase words joined by "
            f"hyphens of at most {NAME_MAX} characters"
        )
    description = fields.get("description", "")
    if not description:
        problems.append("frontmatter description is missing or empty")
    elif len(description) > DESCRIPTION_MAX:
        problems.append(
            f"frontmatter description is {len(description)} characters, "
            f"over the {DESCRIPTION_MAX} limit"
        )
    if flake_nix is None:
        problems.append("flake.nix is missing")
    else:
        flake_names = SKILL_NAME_IN_FLAKE.findall(flake_nix)
        if flake_names != [dir_name]:
            problems.append(
                f"flake.nix skillName {flake_names!r} does not match {dir_name!r}"
            )
    for target in relative_links(skill_md):
        if target not in existing_files:
            problems.append(f"SKILL.md links to {target!r}, which does not exist")
    return problems


def read_or_none(path):
    return path.read_text(encoding="utf-8") if path.is_file() else None


def default_skills_dir():
    """Return the repository's `skills/`: under `$PRJ_ROOT` in the dev shell."""
    return Path(os.environ.get("PRJ_ROOT", ".")) / "skills"


def build_parser():
    parser = argparse.ArgumentParser(
        prog="skill-structure",
        description="Check the skills in this repository for well-formed structure.",
    )
    commands = parser.add_subparsers(dest="command", metavar="COMMAND", required=True)
    check = commands.add_parser(
        "check",
        help="check every skill under a skills directory",
        description=__doc__.strip().split("\n\nRun as")[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    check.add_argument(
        "skills_dir",
        metavar="SKILLS_DIR",
        nargs="?",
        type=Path,
        help="directory holding one subdirectory per skill "
        "(default: $PRJ_ROOT/skills, or ./skills outside the dev shell)",
    )
    return parser


def check(skills_dir):
    """Print each skill's problems; return the exit status."""
    if not skills_dir.is_dir():
        print(f"{skills_dir} is not a directory", file=sys.stderr)
        return 2
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f"no skills found under {skills_dir}", file=sys.stderr)
        return 1
    failed = False
    for skill_dir in skill_dirs:
        existing = {str(p.relative_to(skill_dir)) for p in skill_dir.rglob("*")}
        problems = skill_problems(
            skill_dir.name,
            read_or_none(skill_dir / "SKILL.md"),
            read_or_none(skill_dir / "flake.nix"),
            existing,
        )
        for problem in problems:
            print(f"{skill_dir.name}: {problem}", file=sys.stderr)
        failed = failed or bool(problems)
    if not failed:
        print(f"{len(skill_dirs)} skills well formed")
    return 1 if failed else 0


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.command == "check":
        return check(args.skills_dir or default_skills_dir())
    raise AssertionError(f"unhandled command {args.command!r}")


if __name__ == "__main__":
    sys.exit(main())
