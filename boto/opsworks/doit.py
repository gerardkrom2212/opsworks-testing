#!/usr/bin/env python
import subprocess, sys
from time import sleep
from myboto3 import instances_from_hostname_and_stack

if 0 != subprocess.call(['./create-stack.py']):
    print("Something wrong in creating stack")
    sys.exit(1)

if 0 != subprocess.call(['./create-db-layer.py']):
    print("Something wrong in creating DB layer")
    sys.exit(2)

if 0 != subprocess.call(['./create-db-instances.py']):
    print("Something wrong in creating db instances")
    sys.exit(3)

if 0 != subprocess.call(['./start-stack.py']):
    print("Something wrong in starting instances in DB layer")
    sys.exit(4)

if 0 != subprocess.call(['./create-app-layer.py']):
    print("Something wrong in creating app layer")
    sys.exit(5)

# db has to be runnning for us to start the app boxes the
# first time.
# FIXME: we need to see if db is up, not just that server is up.
db_master = 'db-master1';
done = False
i = 0
while not done:
    instances = instances_from_hostname_and_stack(db_master, 'BotoTest')
    if instances is None:
        print("No instances of %s instances found" % db_master)
    else:
        for instance in instances:
            state = instance['State']['Name']
            if i % 100 == 0:
                print("%s state: %s" % (db_master, state))
            i += 1
            if state == 'running':
                done = True
                break
            pass
        pass
    sleep(5)
    pass

if 0 != subprocess.call(['./create-app-instances.py']):
    print("Something wrong in creating app instances")

if 0 != subprocess.call(['./start-stack.py']):
    print("Something wrong in starting instances in app layer")
    sys.exit(6)

if 0 != subprocess.call(['./create-lb.py']):
    print("Something wrong in load balancer")
    sys.exit(1)

if 0 != subprocess.call(['./lb-register-app-instances.py']):
    print("Something wrong in registering instancess with the load balancer")
    sys.exit(7)

sys.exit(0)
