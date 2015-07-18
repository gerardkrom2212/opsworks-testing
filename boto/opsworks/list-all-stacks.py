#!/usr/bin/env python
"""Print the names of the OpsWorks stacks defined"""
import sys
from myboto3 import stackNames

import pprint
pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) != 1:
    print("""usage:
list-all-stacks

Print the names of the OpsWorks stacks defined
""")
    sys.exit(1)

print(', '.join(stackNames()))
