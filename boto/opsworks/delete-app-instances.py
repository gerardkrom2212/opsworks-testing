#!/usr/bin/env python
import os, sys
import botocore.exceptions
from myboto3 import ops_client, elb_client, stackNames, stackId_from_name
from myboto3 import layerId_from_stackId_and_name

LAST_APP_NUM = 1
LAST_DB_NUM = 1

def register_app_instance(instanceId, elb_client,
                          lbName='CachetLoadBalancer'):
    response = elb_client.register_instances_with_load_balancer(
        LoadBalancerName=lbname,
        Instances[{'instanceId': instanceId}])
    print(response)
    return

def create_app_instance(stackName, client, layerName='PHP App Servers',
                        hostname=None):
    global LAST_APP_NUM
    stackId = stackId_from_name(stackName)
    if stackId is None:
        print("Can't find stack %s; nothing done" % stackName)
        return False

    layerId = layerId_from_stackId_and_name(stackId, layerName)
    if layerId is None:
        print("Can't find layer %s in stack %s; nothing done" %
              (layerName, stackName))
        return False

    host_name = 'cachet-app%d' % LAST_APP_NUM
    try:
        result = client.create_instance(

                  # Required parameters
                  StackId=stackId,
                  LayerIds=[layerId],
                  InstanceType='t2.micro',

                  # Optional parameters
                  Hostname = host_name,
                  # SshKeyName='string',
                  Architecture = 'x86_64',
                  )
        LAST_APP_NUM += 1
        instanceId = result['InstanceId']
        print("instance %s in layer %s of stack %s created" %
              (instanceId, layerName, stackName))
        register_app_instance(instanceId, elb_client)
        print(result)
    except botocore.exceptions.ClientError as e:
        print e
        return False
    return True

def create_db_instance(stackName, client, layerName='MySQL DB',
                        hostname=None):
    global LAST_APP_NUM
    stackId = stackId_from_name(stackName)
    if stackId is None:
        print("Can't find stack %s; nothing done" % stackName)
        return False

    layerId = layerId_from_stackId_and_name(stackId, layerName)
    if layerId is None:
        print("Can't find layer %s in stack %s; nothing done" %
              (layerName, stackName))
        return False

    host_name = 'db-master%d' % LAST_APP_NUM
    try:
        result = client.create_instance(

                  # Required parameters
                  StackId=stackId,
                  LayerIds=[layerId],
                  InstanceType='t2.micro',

                  # Optional parameters
                  Hostname = host_name,
                  # SshKeyName='string',
                  Architecture = 'x86_64',
                  )
        LAST_APP_NUM += 1
        print("instance in layer %s of stack %s created" %
              (layerName, stackName))
        print(result)
    except botocore.exceptions.ClientError as e:
        print e
        return False
    return True


if not(1 <= len(sys.argv) <= 2):
    print("""usage:
%s [*StackName*]

Create the OpsWorks instances for the php cachet system
The default stack name is BotoTest.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

stackName = 'BotoTest'
if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName not in stackNames():
    print("Stack %s doesn't exist; nothing done" % stackName)
    sys.exit(2)

create_app_instance(stackName, ops_client)
#create_db_instance(stackName, ops_client)
