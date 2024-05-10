#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET "$1" -w "%{http_code}" | awk '/200/ {p=1; next} p' | sed '1d'
