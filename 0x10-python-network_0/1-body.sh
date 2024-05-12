#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response if the status code is 200
curl -s -X GET -w "%{http_code}" "$1" | awk '/200/{p=1;next}p' | tail -n +2
