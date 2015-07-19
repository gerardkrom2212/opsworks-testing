#!/usr/bin/env python
import os, sys
from myboto3 import ops_client, stackNames, stackId_from_name
from myboto3 import instanceIds_from_stack

stackName = 'BotoTest'
if not (0 < len(sys.argv) <= 2):
    print("""usage:
%s [*StackName*]

Delete OpsWorks stack *StackName*. If no *StackName* is given we use
%s.
""" % (os.path.basename(sys.argv[0]), stackName))
    sys.exit(1)

if len(sys.argv) == 2: stackName = sys.argv[1]

stackId = stackId_from_name(stackName)
if stackId is None:
    print("Cant find Stack %s" % stackName)
    sys.exit(2)

result = ops_client.delete_stack(StackId=stackId)
print(result)
