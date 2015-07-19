#!/usr/bin/env python
import os, sys
from myboto3 import instanceId_from_hostname

if len(sys.argv) != 3:
    print("""usage: %s *hostname* *layer-name*

Get an ec2-instance id from a hostname
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

host_name, layerName  = sys.argv[1:]
ec2InstanceId = instanceId_from_hostname(host_name, layerName)
if ec2InstanceId is not None:
    print("Host %s has instance id %s" % (host_name, ec2InstanceId))
else:
    print("Cant find instance id for host %s in layer %s" % (host_name, layerName))
