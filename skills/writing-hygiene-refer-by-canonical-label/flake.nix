{
  description = "writing-hygiene-refer-by-canonical-label: Agent skill — refer to each issue, pull request, commit, file or event by one canonical label, linked, with machine identifiers in parentheses after it";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    agent-skill-flake.url = "github:nhooey/agent-skill-flake";
    agent-skill-flake.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs =
    { nixpkgs, agent-skill-flake, ... }:
    agent-skill-flake.lib.mkSkillFlake {
      inherit nixpkgs;
      source = import ../../source.nix;
      skillName = "writing-hygiene-refer-by-canonical-label";
      src = ./.;
    };
}
