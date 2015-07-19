#!/bin/bash
if ! ./create-stack.py ; then
    echo "Something wrong in creating stack"
    exit 1
fi
if ! ./create-db-layer.py ; then
    echo "Something wrong in creating DB layers"
    exit 2
fi
if ! ./create-app-layer.py ; then
    echo "Something wrong in creating app layers"
    exit 3
fi
if ! ./create-db-instances.py ; then
    echo "Something wrong in creating db instances"
    exit 4
fi
if ! ./create-app-instances.py ; then
    echo "Something wrong in creating app instances"
fi
exit 0
