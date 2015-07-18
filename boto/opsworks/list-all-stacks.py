#!/usr/bin/env python
"""Print the names of the OpsWorks stacks defined"""
import os,sys
from myboto3 import stackNames

import pprint
pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) != 1:
    print("""usage:
%s

Print the names of the OpsWorks stacks defined
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

print(', '.join(stackNames()))
