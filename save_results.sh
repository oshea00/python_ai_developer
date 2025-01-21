#!/bin/bash

# This script copies the generated code, research results and test results to a folder named after the experiment name

# check for experiment name in $1 if none exit with help message
if [ -z "$1" ]; then
    echo "Usage: $0 <experiment_name>"
    exit 1
fi

mkdir -p results/$1

cp generated_code.py results/$1/
cp research_results.md results/$1/
cp test_results.md results/$1/

