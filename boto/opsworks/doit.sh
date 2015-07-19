#!/bin/bash
if ! ./create-stack.py ; then
    echo "Something wrong in creating stack"
    exit 1
fi
if ! ./create-all-layers.py ; then
    echo "Something wrong in creating layers"
    exit 2
fi
if ! ./create-db-instances.py ; then
    echo "Something wrong in creating db instances"
fi
if ! ./create-php-instances.py ; then
    echo "Something wrong in creating app instances"
fi
exit 0
