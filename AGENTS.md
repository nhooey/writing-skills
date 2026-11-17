# writing-skills

Agent skills for what to say and how to structure it, for any author in any
format, packaged as a Nix flake built by
[agent-skill-flake](https://github.com/nhooey/agent-skill-flake). Each skill
is a directory under `skills/` with a `SKILL.md` and its own `flake.nix`.

## Build and test

- `nix develop`: enter the dev shell, which installs the skills from the
  `skills-devshell/` sub-flake into `.agents/skills/`; run `menu` to list
  its commands.
- `fmt`: format the repository, nixfmt over `*.nix` and prettier over
  `*.md` and `*.yaml`.
- `check`: run `nix flake check`, which checks that every file is
  formatted and runs the checks agent-skill-flake's dev shell module adds.
- Skill structure is held by agent-skill-flake's `skill-layout` and
  `skill-description` checks: SKILL.md frontmatter is a strict-YAML
  mapping, its `name` matches the skill's directory, its `description` is
  within 1,024 characters, the skill's `flake.nix` builds the same
  `skillName`, and relative links resolve. They read their settings from
  `skill-checks.toml`, which turns on the `skill-flake` rule.
- agent-skill-flake's `skill-description` check holds each skill listed
  under `trigger-first` in `skill-checks.toml` to a description that opens
  on `Load ` and stays within 500 characters.
- To run those checks from a checkout of agent-skill-flake rather than the
  version `flake.lock` pins:

  ```bash
  nix flake check --override-input agent-skill-flake path:<agent-skill-flake checkout> --no-write-lock-file
  ```
