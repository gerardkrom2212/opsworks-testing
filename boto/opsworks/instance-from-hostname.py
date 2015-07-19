#!/usr/bin/env python
import os, sys
from myboto3 import instanceId_from_hostname_and_stack

if not (2 <= len(sys.argv) <= 3):
    print("""usage: %s *hostname* [*stackname*]

Get an ec2-instance id from a hostname. If stackname is given,
narrow host to hosts in that stack.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

hostname = sys.argv[1]
stackName=None
if len(sys.argv) == 3: stackName = sys.argv[2]
ec2InstanceId = instanceId_from_hostname_and_stack(hostname, stackName)
if ec2InstanceId is not None:
    print("Host %s has instance id %s" % (hostname, ec2InstanceId))
else:
    print("Cant find instance id for host %s" % host_name)
