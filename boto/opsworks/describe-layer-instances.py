#!/usr/bin/env python
"""Prints Opsworks Layer Information for a stack"""
import os, sys
from myboto3 import ops_client, stackId_from_name
from myboto3 import layerId_from_stackId_and_name

# Some defaults
stackName = 'BotoTest'
layerName = "PHP App Servers"
full = False

if not(1 <= len(sys.argv) <= 4):
    print("""Usage:
%s [*StackName* [*Layer*] [full]]

Gets Opworks instances host names for Stack *StackName* and
layer %. If no stack name is given use %s.

If no layer name given use %s.""" %
          (os.path.basename(sys.argv[0]), stackName, layerName))
    sys.exit(1)

if len(sys.argv) >= 2: stackName = sys.argv[1]
if len(sys.argv) >= 3: layerName = sys.argv[2]
if len(sys.argv) == 4 and sys.argv[3] == 'full':
    full = True


stackId = stackId_from_name(stackName)
if stackId is None:
    print("Didn't find stack %s" % stackName)
    sys.exit(2)

layerId = layerId_from_stackId_and_name(stackId, layerName)
if layerId is None:
    print("Didn't find layer %s in stack %s" % (layerName, stackName))
    sys.exit(2)

resp = ops_client.describe_instances(LayerId=layerId)

if full:
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(resp)
else:
    hosts = [instance['Hostname'] for instance in resp['Instances']]
    print(', '.join(hosts))


sys.exit(0)
