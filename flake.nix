{

  description = "Python Playground for testing Python features";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    rust-overlay.url = "github:oxalica/rust-overlay";
    pyproject-nix.url = "github:nix-community/pyproject.nix";
    uv2nix.url = "github:adisbladis/uv2nix";
  }; # inputs

  outputs =
    inputs@{
      self,
      nixpkgs,
      flake-parts,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        # "aarch64-linux"
        # "x86_64-darwin"
        # "aarch64-darwin"
      ];
      # This config is still good practice, but we will create our own pkgs for clarity.
      flake.nixpkgs.config = {
        allowUnfree = true;
      };
      flake.nixpkgs.overlays = [ inputs.rust-overlay.overlays.default ];

      perSystem =
        {
          system,
          ...
        }:
        let

          pkgs = import nixpkgs {
            inherit system;
            config.allowUnfree = true;
            # overlays = [ inputs.rust-overlay.overlays.default ];
          };

          inputPackages = builtins.attrValues {
            inherit (pkgs)
              uv
              # # For scipy
              # gfortran
              # blas
              # lapack

              # # For pygobject, matplotlib
              # pkg-config
              gtk3
              gobject-introspection
              cairo
              librsvg
              fontconfig
              dejavu_fonts
              # pango
              # gdk-pixbuf
              # fontconfig
              # freetype
              # tcl
              # tk

              # # General
              # openssl
              # zlib
              # libffi
              ;
          }; # inputPackages

          libraries = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc.lib
            pkgs.gfortran.cc.lib
            pkgs.glibc
            pkgs.zlib
            # pkgs.libffi
            # pkgs.openssl
            # pkgs.blas
            # pkgs.lapack
            # pkgs.xorg.libX11
            # pkgs.xorg.libXext
            # pkgs.xorg.libXrender
            # pkgs.xorg.libXtst
            # pkgs.cairo
            # pkgs.pango
            # pkgs.gdk-pixbuf
            # pkgs.gtk3
            # pkgs.gobject-introspection
            # pkgs.fontconfig
            # pkgs.freetype
            # pkgs.tcl
            # pkgs.tk
            # pkgs.qt5.qtbase

          ];

        in
        {
          devShells.default = pkgs.mkShell {
            name = "DSP Python FIR and IIR Tools";

            buildInputs = inputPackages;

            env.NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";
            env.NIX_LD_LIBRARY_PATH = libraries;
            env.NIX_ALLOW_UNFREE = 1;

            env.FONTCONFIG_FILE = "${pkgs.fontconfig}/etc/fonts/fonts.conf";
            env.FONTCONFIG_PATH = "${pkgs.fontconfig}/etc/fonts";

            # env.MPLBACKEND = "GTK3Agg";

            # env.LD_LIBRARY_PATH = libraries;

            # env.TK_LIBRARY = "${pkgs.tk}/lib/${pkgs.tk.libPrefix}";
            # env.TCL_LIBRARY = "${pkgs.tcl}/lib/${pkgs.tcl.libPrefix}";

            # env.QT_QPA_PLATFORM_PLUGIN_PATH = "${pkgs.qt5.qtbase.bin}/lib/qt-${pkgs.qt5.qtbase.version}/plugins";

            shellHook = ''
              echo "Activating environment..."
              uv sync
              source .venv/bin/activate
              uv lock --upgrade
            ''; # shellHook

          }; # devShells.default

        }; # perSystem

    }; # flake-parts.lib.mkFlake

}
