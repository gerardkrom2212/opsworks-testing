#!/usr/bin/env python
"""Prints Opsworks stack information"""
import sys
from myboto3 import client, stackId_from_name

import pprint
pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) != 2:
    print("""Usage:
describe-stack *StackName*

Gets Opworks stack information for Stack *StackName*
""")
    sys.exit(1)

stackName = sys.argv[1]
stackId = stackId_from_name(stackName)
if stackId is not None:
    ss = client.describe_stacks(StackIds=[stackId])
    pp.pprint(ss)
    sp = client.describe_stack_provisioning_parameters(StackId=stackId)
    print('-' * 40)
    pp.pprint(sp)
    sys.exit(0)
else:
    print("Didn't find stack %s" % stackName)
    sys.exit(2)
