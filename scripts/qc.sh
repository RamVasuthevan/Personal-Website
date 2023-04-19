#!/bin/bash

# Check if an argument is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a branch name as an argument."
    exit 1
fi

# Set variables
arg1="$*"
remote_branch="main"

# Convert argument to lowercase and replace spaces with underscores
new_branch_name=$(echo "$arg1" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

# Run git commands
git checkout $remote_branch
git pull
git checkout -b $new_branch_name
git add .
git commit -m "$arg1"
