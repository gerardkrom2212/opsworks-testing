#!/bin/bash
if ! ./create-stack.py ; then
    echo "Something wrong in creating stack"
    exit 1
fi
if ! ./create-db-layer.py ; then
    echo "Something wrong in creating DB layer"
    exit 2
fi
if ! ./create-db-instances.py ; then
    echo "Something wrong in creating db instances"
    exit 3
fi

# Starting everything when DB exists, starts
# gives us a head start on the DB before starting
if ! ./start-stack.py ; then
    echo "Something wrong in starting instances in DB layer"
    exit 4
fi
if ! ./create-app-layer.py ; then
    echo "Something wrong in creating app layer"
    exit 5
fi

# FIXME: This is a hack to attempt to make sure db comes up before
# app.

sleep 300
if ! ./create-app-instances.py ; then
    echo "Something wrong in creating app instances"
fi
if ! ./start-stack.py ; then
    echo "Something wrong in starting instances in app layer"
    exit 6
fi
if ! ./lb-register-app-instances.py ; then
    echo "Something wrong in registering instancess with the load balancer"
    exit 7
fi
exit 0
