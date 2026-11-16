# writing-skills

Agent skills for what to say and how to structure it, for any author in any
format, packaged as a Nix flake built by
[agent-skill-flake](https://github.com/nhooey/agent-skill-flake). Each skill
is a directory under `skills/` with a `SKILL.md` and its own `flake.nix`.

## Build and test

- `nix develop`: enter the dev shell, which installs the skills from the
  `skills-devshell/` sub-flake into `.agents/skills/`; run `menu` to list
  its commands.
- `fmt`: format the repository, nixfmt over `*.nix`, prettier over
  `*.md` and `*.yaml`, and ruff over `*.py`.
- `check`: run `nix flake check`, which checks that every file is
  formatted, runs `skill-structure check` over `skills/` and runs the
  checker's unit tests in `tests/test_skill_structure.py`.
- `skill-structure check [SKILLS_DIR]`: check every skill is well formed
  (frontmatter name matches its directory, description within 1024
  characters, `flake.nix` builds the same `skillName`, relative links
  resolve), without the rest of `check`. The tool lives in
  `tests/skill_structure.py`.
