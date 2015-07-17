#!/usr/bin/env python
import sys
from myboto3 import client, stackNames, stackId_from_name, layerId_from_stackId_and_name

if not (1 <= len(sys.argv) <= 2):
    print("""usage:
delete-layers [*StackName*]

Delete all OpsWorks layers in stack *StackName*. If no
*StackName* is given we use BotoTest
""")
    sys.exit(1)

stackName = 'BotoTest'
if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName not in stackNames():
    print("Stack %s doesn't exists, nothing done" % stackName)
    sys.exit(2)

stackId = stackId_from_name(stackName)
if stackId is None:
    print("Can't find stack with name %s" % stackName)
    sys.exit(3)

resp = client.describe_layers(StackId=stackId)
count = 0
for layer in resp['Layers']:
    count += 1
    result = client.delete_layer(LayerId=layer['LayerId'])
    print("Layer %s of %s deleted" % (layer['Name'], stackName))
    print(result)
print("Total of %d layer(s) deleted" % count)
