#!/usr/bin/env python
import os, sys
from myboto3 import ops_client, stackNames, stackId_from_name, layerId_from_stackId_and_name

if not (1 < len(sys.argv) <= 2):
    print("""usage:
%s *layerName* [*StackName*]

Delete OpsWorks layer *layerName in stack *StackName*. If no
*StackName* is given we use BotoTest
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

layerName = sys.argv[1]
stackName = 'BotoTest'
if len(sys.argv) == 3: stackName = sys.argv[2]

if stackName not in stackNames():
    print("Stack %s doesn't exists, nothing done" % stackName)
    sys.exit(2)

stackId = stackId_from_name(stackName)
if stackId is None:
    print("Can't find stack with name %s" % stackName)
    sys.exit(3)

layerId = layerId_from_stackId_and_name(stackId, layerName)
if layerId is None:
    print("Can't find layer in stack %s with name %s" % (layerName, stackName))
    sys.exit(4)

print("Layer %s of %s deleted" % (layerName, stackName))
result = ops_client.delete_layer(LayerId=layerId)
print(result)
