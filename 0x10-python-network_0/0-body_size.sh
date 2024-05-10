#!/bin/bash
# Get response size from URL using curl

curl -s "$1" | grep -iE '^Content-Length: ([0-9]+)' | awk '{print $2}'
