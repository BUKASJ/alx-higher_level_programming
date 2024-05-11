#!/usr/bin/python3
"""
This script fetches the url and displays the body response.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
