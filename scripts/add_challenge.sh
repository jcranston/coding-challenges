#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <challenge_name>"
    exit 1
fi

CHALLENGE_NAME="$1"
TEMPLATE_DIR="challenges/template"
NEW_CHALLENGE_DIR="challenges/$CHALLENGE_NAME"

if [ -d "$NEW_CHALLENGE_DIR" ]; then
    echo "Error: $NEW_CHALLENGE_DIR already exists."
    exit 1
fi

cp -r "$TEMPLATE_DIR" "$NEW_CHALLENGE_DIR"
echo "Created new challenge: $NEW_CHALLENGE_DIR" 

# Ensure __init__.py exists in the new challenge directory
if [ ! -f "$NEW_CHALLENGE_DIR/__init__.py" ]; then
    touch "$NEW_CHALLENGE_DIR/__init__.py"
fi 