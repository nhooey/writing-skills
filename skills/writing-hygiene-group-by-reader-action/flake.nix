{
  description = "writing-hygiene-group-by-reader-action: Agent skill — sort a long, flat run of items into groups by the attribute the reader acts on, each group headed by its value and count, in order of importance, each kind marked by one emoji";

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
      skillName = "writing-hygiene-group-by-reader-action";
      src = ./.;
    };
}
