#!/usr/bin/env python
import os, sys
from myboto3 import ops_client, stackId_from_name

stackName = 'BotoTest'
if not (1 <= len(sys.argv) <= 2):
    print("""usage: %s [*stackname*]

Starts all instances in *stackname*.
If *stackname* is not given, we use BotoTest.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) == 2: stackName = sys.argv[1]

stackId = stackId_from_name(stackName)
if stackId is None:
    print("Can't find stack %s" % stackName)
    sys.exit(2)

result = ops_client.start_stack(StackId=stackId)
print(result)
