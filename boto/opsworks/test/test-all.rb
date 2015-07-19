#!/usr/bin/env ruby
[
    %w(../list-all-stacks.py),
    %w(../list-all-stacks.py a bogus),
    %w(../list-stack-instances.py BotoTest),
    %w(../list-stack-instances.py bogus),
    %w(../create-stack.py t1),
    %w(../create-stack.py t1 a bogus),
    %w(../create-all-layers.py t1),
    %w(../create-all-layers.py t1 bogus),
    %w(../delete-all-layers.py t1),
    %w(../delete-all-layers.py t1 bogus),
    %w(../delete-stack.py t1),
    %w(../delete-stack.py t1 bogus),
].each do |cmd|
    puts cmd.join(', ')
    system(*cmd)
    puts '-' * 40
end
