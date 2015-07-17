#!/usr/bin/env python
import sys
from myboto3 import client, stackNames, stackId_from_name

if not (0 < len(sys.argv) <= 2):
    print("""usage:
delete-stack [*StackName*]

Delete OpsWorks stack *StackName*. If no *StackName* is given we use
BotoTest
""")
    sys.exit(1)

stackName = 'BotoTest'
if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName not in stackNames():
    print("Stack %s doesnt exists, nothing done" % stackName)
    sys.exit(2)

stackId = stackId_from_name(stackName)
if stackId is not None:
    result = client.delete_stack(StackId=stackId)
    print(result)
