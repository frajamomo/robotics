#!/bin/bash

COUNTER=1

if [ "$#" -gt 0 ]
then
    for i in "$@"
    do
        echo "Argument $COUNTER is $i"
        ((COUNTER++))
    done
else
    echo "No arguments passed to the script."
fi
