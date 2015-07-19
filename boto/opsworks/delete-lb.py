#!/usr/bin/env python
import os, sys
from myboto3 import elb_client, lbNames, stackId_from_name

lbName = 'CachetLoadBalancer'
if not (0 < len(sys.argv) <= 2):
    print("""usage: %s [*LoadBalancerName*]

Delete load lalancer *LoadBalancerName*. If no *LoadBalancerName* is given
we use %s.""" % (os.path.basename(sys.argv[0]), lbName))
    sys.exit(1)

if len(sys.argv) == 2: lbName = sys.argv[1]

if lbName not in lbNames():
    print("Load Balancer %s doesn't exists, nothing done" % lbName)
    sys.exit(2)

result = elb_client.delete_load_balancer(LoadBalancerName=lbName)
print(result)
