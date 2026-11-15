# writing-skills

Agent skills for what to say and how to structure it, for any author in any
format, packaged as a Nix flake built by
[agent-skill-flake](https://github.com/nhooey/agent-skill-flake). Each skill
is a directory under `skills/` with a `SKILL.md` and its own `flake.nix`.

## Build and test

- `nix develop`: enter the dev shell, which installs the skills from the
  `skills-devshell/` sub-flake into `.agents/skills/`; run `menu` to list
  its commands.
- `nix fmt`: format the repository, nixfmt over `*.nix` and prettier over
  `*.md` and `*.yaml`.
- `nix flake check`: check the flake, including that every file is
  formatted.
