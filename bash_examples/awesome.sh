#!/bin/bash

if [[ $1 == "me" ]]; then
    echo "Yes, I'am awesome.";
elif [[ $1 == "them" ]]; then
    echo "Okay, they are awesome.";
else
    echo "Usage ./awesome.sh me|them";
fi
