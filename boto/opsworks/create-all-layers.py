#!/usr/bin/env python
import os, sys
import botocore.exceptions
from myboto3 import ops_client, stackNames, stackId_from_name
from myboto3 import instananceId_from_hostname

def create_app_layer(stackName, client):
    stackId = stackId_from_name(stackName)
    if stackId is None:
        print("Can't find stack %s; nothing done" % stackName)
        return False

    try:
        result = client.create_layer(
            # Required parameters
            StackId=stackId,
            Type='php-app',
            Name='PHP App Servers',
            Shortname='PHP App Servers',

            # Optional parameters
            CustomRecipes =  {
                'Setup': [   'mash::devpkgs',
                             'mash::phpcomposer',
                             'mash::cachetsetup'],
                }
            )
        print("PHP APP layer in stack %s created" % stackName)
        print(result)
    except botocore.exceptions.ClientError as e:
        print e
        return False
    return True

def create_db_layer(stackName, client):
    stackId = stackId_from_name(stackName)
    if stackId is None:
        print("Can't find stack %s; nothing done" % stackName)
        return False

    try:
        result = client.create_layer(
            # Required parameters
            StackId=stackId,
            Type='db-master',
            Name='MySQL DB',
            Shortname='MySQL DB',

            # Optional parameters
            Attributes={
                'MysqlRootPassword' : 'secret',
                'MysqlRootPasswordUbiquitous': 'true',
                },
            CustomRecipes =  {
                'Setup': ['mash::devpkgs', 'mash::dbsetup'],
                },

            )

        print("DB layer in stack %s created" % stackName)
        print(result)
    except botocore.exceptions.ClientError as e:
        print e
        return False

    return True

if not(1 <= len(sys.argv) <= 2):
    print("""usage:
%s [*StackName*]

Create the OpsWorks layers for the php cachet system
The default stack name is BotoTest.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

stackName = 'BotoTest'
if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName not in stackNames():
    print("Stack %s doesn't exist; nothing done" % stackName)
    sys.exit(2)

create_app_layer(stackName, ops_client)
create_db_layer(stackName, ops_client)
