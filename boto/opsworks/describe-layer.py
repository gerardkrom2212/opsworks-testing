#!/usr/bin/env python
"""Prints Opsworks Layer Information for a stack"""
import sys
from myboto3 import client, stackId_from_name

import pprint
pp = pprint.PrettyPrinter(indent=4)


# Some defaults
stackName = 'BotoTest'
layer = "PHP App Servers"

if not(1 <= len(sys.argv) <= 3):
    print("""Usage:
describe-layers [*StackName* [*Layer*]]

Gets Opworks layer information for Stack *StackName*. If no stack name
is given use %s.

If no layer name given use %s""" % (stack, layer))
    sys.exit(1)

if len(sys.argv) >= 2: stackName = sys.argv[1]
if len(sys.argv) == 3: layer = sys.argv[2]

stackId = stackId_from_name(stackName)
if stackId is not None:
    layers = client.describe_layers(StackId=stackId)
    pp.pprint(layers)
    sys.exit(0)
else:
    print("Didn't find stack %s" % stackName)
    sys.exit(2)
