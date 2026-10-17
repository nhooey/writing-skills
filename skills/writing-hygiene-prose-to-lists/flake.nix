{
  description = "writing-hygiene-prose-to-lists: Agent skill — rewrite prose that is really an enumeration, hierarchy or set of options as a nested list, faithfully, and leave real narrative alone";

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
