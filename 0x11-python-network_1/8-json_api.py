#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to the url
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    data = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                  json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
