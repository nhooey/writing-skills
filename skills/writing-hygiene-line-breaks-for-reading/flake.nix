{
  description = "writing-hygiene-line-breaks-for-reading: Agent skill — break lines in code and config for the reader, never pack items onto a line to save lines or by width, keep config and manifest list literals one element per line, and keep it that way under nixfmt, prettier, black and ruff";

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
      skillName = "writing-hygiene-line-breaks-for-reading";
      src = ./.;
    };
}
