{
  description = "writing-hygiene-declarative-statements: Agent skill — write every artifact as state: a snapshot says what is true, a delta says what became true (before → after), and neither narrates the steps";

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
      skillName = "writing-hygiene-declarative-statements";
      src = ./.;
    };
}
