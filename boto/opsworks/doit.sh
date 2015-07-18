#!/bin/bash
if ! ./create-stack.py ; then
    echo "Something wrong in creating stack"
    exit 1
fi
if ! ./create-all-layers.py ; then
    echo "Something wrong in creating layers"
    exit 2
fi
if ! ./create-all-instances.py ; then
    echo "Something wrong in creating instances"
fi
exit 0
