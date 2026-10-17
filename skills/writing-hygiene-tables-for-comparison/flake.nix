{
  description = "writing-hygiene-tables-for-comparison: Agent skill — lift items described against the same properties into a comparison table, items in rows, only differing properties as columns";

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
      skillName = "writing-hygiene-tables-for-comparison";
      src = ./.;
    };
}
