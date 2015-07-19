#!/usr/bin/env python
"""Print the names of the OpsWorks stacks defined"""
import os, sys
from myboto3 import lbNames, elb_client

full = False
if not (1 <= len(sys.argv) <= 2):
    print("""usage: %s [full]

Print the names of the Load Balancers defined.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) == 2 and sys.argv[1] == 'full': full = True

if full:
    lbs = elb_client.describe_load_balancers()
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(lbs)
else:
    print(', '.join(lbNames()))
