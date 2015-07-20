#!/usr/bin/env python
import os, sys
import botocore.exceptions
from myboto3 import ops_client, elb_client, ec2_client
from myboto3 import stackNames, stackId_from_name
from myboto3 import layerId_from_stackId_and_name
from myboto3 import instanceId_from_hostname_and_stack

def register_app_instance(instanceId, elb_client,
                          lbName='CachetLoadBalancer'):
    try:
        response = elb_client.register_instances_with_load_balancer(
            LoadBalancerName = lbName,
            Instances = [{'InstanceId': instanceId}])
        print(response)
    except botocore.exceptions.ClientError as e:
        print(e)
    return

layerName = 'PHP App Servers'
for i in range(1,4):
    hostname = 'cachet-app%d' % i
    ec2InstanceId = instanceId_from_hostname_and_stack(hostname, 'BotoTest')
    if ec2InstanceId is not None:
        register_app_instance(ec2InstanceId, elb_client)
        print("Registered %s in load balancer" % ec2InstanceId)
