#!/bin/bash
# Get response size from URL using curl

curl -sI "$1" | awk '/Content-Length/ {print $2}'
