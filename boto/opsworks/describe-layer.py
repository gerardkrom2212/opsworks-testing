#!/usr/bin/env python
"""Prints Opsworks Layer Information for a stack"""
import os, sys
from myboto3 import ops_client, stackId_from_name

import pprint
pp = pprint.PrettyPrinter(indent=4)


# Some defaults
stackName = 'BotoTest'
layerName = "PHP App Servers"

if not(1 <= len(sys.argv) <= 3):
    print("""Usage:
%s [*StackName* [*Layer*]]

Gets Opworks layer information for Stack *StackName*. If no stack name
is given use %s.

If no layer name given use %s.""" %
          (os.path.basename(sys.argv[0]), stackName, layerName))
    sys.exit(1)

if len(sys.argv) >= 2: stackName = sys.argv[1]
if len(sys.argv) == 3: layerName = sys.argv[2]

stackId = stackId_from_name(stackName)
if stackId is None:
    print("Didn't find stack %s" % stackName)
    sys.exit(2)

layers = ops_client.describe_layers(StackId=stackId)
pp.pprint(layers)
sys.exit(0)
