#!/usr/bin/env python
import os, sys
from myboto3 import elb_client, lbNames

lbName = 'CachetLoadBalancer'
if not(1 <= len(sys.argv) <= 2):
    print("""usage: %s [*LoadBalancerName*]

Create elastic load balancer for php cachet test application.
The default stack is %s.""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) == 2: lbName = sys.argv[1]

if lbName in lbNames():
    print("Load Balancer %s already exists, nothing done" % lbName)
    sys.exit(2)

# FIXME: turn 'AWS-OpsWorks-PHP-App-Server'
# info 'sg-8366a4e4'
result = elb_client.create_load_balancer(
    # Required parameters
    LoadBalancerName=lbName,

    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 8000,
        },
    ],
    AvailabilityZones = ['us-east-1a',
                         'us-east-1c','us-east-1d', 'us-east-1e'],
    SecurityGroups = ['sg-8366a4e4'],
    )
print(result)
