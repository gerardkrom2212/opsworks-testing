#!/usr/bin/env python
import os, sys
from myboto3 import instanceIds_from_stack

stackName = 'BotoTest'
if not (1 <= len(sys.argv) <= 2):
    print("""usage: %s [*stackname*]

lists ec2 instances in *stackname*.
If *stackname* is not given, we use BotoTest.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) == 2: stackName = sys.argv[1]

instanceIds = instanceIds_from_stack(stackName)
print("ec2 instances in %s: %s" % (stackName, ', '.join(instanceIds)))
