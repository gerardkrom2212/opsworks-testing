#!/usr/bin/env python
"""Print the names of the OpsWorks stacks defined"""
import os,sys
from myboto3 import stackNames

if len(sys.argv) != 1:
    print("""usage: %s

Print the names of the OpsWorks stacks defined.
""" % os.path.basename(sys.argv[0]))
    sys.exit(1)

print(', '.join(stackNames()))
