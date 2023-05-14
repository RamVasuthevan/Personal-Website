#!/bin/bash

prefix="RamVasuthevan-patch-"
num=1

# Fetch the remote branches
git fetch

# Loop until we find a number that's not used in local and remote branches
while [ $(git branch -a | grep -c "${prefix}${num}") -ne 0 ]; do
  ((num++))
done

# Create the branch
git checkout -b ${prefix}${num}