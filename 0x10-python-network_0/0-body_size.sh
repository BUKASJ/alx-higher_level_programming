#!/bin/bash
#script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

curl -sI $1 | awk '/Content-Length/ {print "Size of the response body: " $2 " bytes"; exit}'
