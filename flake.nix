{
  description = "Flake for Python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/fbcf476f790d8a217c3eab4e12033dc4";
    flake-utils.url = "github:numtide/flake-utils/11707dc2f618dd54ca8739b309ec4fc024de578b";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python313;
        python_packages = python.withPackages (
          ps: with ps; [
            scipy
            black
            matplotlib
          ]
        );
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            python_packages
            pkgs.pyright
          ];
        };
      }
    );
}
