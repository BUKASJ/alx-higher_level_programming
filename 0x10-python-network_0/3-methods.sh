#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
curl -s -I --options "$1" | grep -i 'Allow:' | awk '{print $2}'
