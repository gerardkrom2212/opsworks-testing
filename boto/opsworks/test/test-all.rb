#!/usr/bin/env ruby
[
    %w(../list-all-stacks.py),
    %w(../create-stack.py t1),
    %w(../create-all-layers.py t1),
    %w(../delete-all-layers.py t1),
    %w(../delete-stack.py t1)
].each do |cmd|
    puts cmd.join(', ')
    system(*cmd)
end
