{
  description = "writing-hygiene-prose-to-lists: Agent skill — rewrite an inline run of parallel items, whatever joins them, as a flat or nested list, faithfully, and leave real narrative alone";

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
      skillName = "writing-hygiene-prose-to-lists";
      src = ./.;
    };
}
