#!/bin/bash
set -e

IMAGE_NAME=coding_challenges:latest
CONTAINER_NAME=coding_challenges_dev

if [ "$1" = "build" ]; then
    docker build -t $IMAGE_NAME -f docker/Dockerfile .
    exit 0
fi

if [ "$1" = "run" ]; then
    docker run --rm -it \
        --name $CONTAINER_NAME \
        -v "$(pwd)":/workspace \
        $IMAGE_NAME
    exit 0
fi

echo "Usage: $0 [build|run]"
exit 1 