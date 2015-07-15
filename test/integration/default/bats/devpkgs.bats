#!/usr/bin/env bats
# -*-shell-script-*-

# Development packages that any box should have.
pkgs='emacs bashdb'

@test "$pkg binaries is found in PATH" {
    for pkg in $pkgs; do
	run which $pkg
	[ "$status" -eq 0 ]
    done
}
@test "$pkgs --version runs on each package" {
    for pkg in $pkgs; do
	run $pkg --version
	[ "$status" -eq 0 ]
    done
}
