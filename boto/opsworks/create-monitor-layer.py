#!/usr/bin/env python
import os, sys
import botocore.exceptions
from myboto3 import ops_client, stackNames, stackId_from_name

def create_monitor_layer(stackName, client):
    stackId = stackId_from_name(stackName)
    if stackId is None:
        print("Can't find stack %s; nothing done" % stackName)
        return False

    try:
        result = client.create_layer(
            # Required parameters
            StackId=stackId,
            Type='custom',  # consider monitoring-master
            Name='Monitor',
            Shortname='monitor',

            # Optional parameters
            CustomRecipes =  {
                'Setup': ['mash::devpkgs'],
                },
            )

        print("Monitor layer in stack %s created" % stackName)
        print(result)
    except botocore.exceptions.ClientError as e:
        print e
        return False

    return True

if not(1 <= len(sys.argv) <= 2):
    print("""usage:
%s [*StackName*]

Create the OpsWorks monitor layer for the php cachet system
The default stack name is BotoTest.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

stackName = 'BotoTest'
if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName not in stackNames():
    print("Stack %s doesn't exist; nothing done" % stackName)
    sys.exit(2)

create_monitor_layer(stackName, ops_client)
