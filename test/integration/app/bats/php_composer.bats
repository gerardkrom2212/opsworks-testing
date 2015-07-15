#!/usr/bin/env bats
# -*-shell-script-*-

run which $pkg
[ "$status" -eq 0 ]

 run $pkg -V
 [ "$status" -eq 0 ]
