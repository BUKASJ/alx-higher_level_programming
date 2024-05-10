#!/bin/bash
#script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

url=$1

response=$(curl -sI $url | grep -i 'content-length' | awk '{print $2}' | tr -d '\r')

echo "Size of the response body: $response bytes"
