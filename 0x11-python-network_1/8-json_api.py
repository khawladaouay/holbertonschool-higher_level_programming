#!/usr/bin/python3
"""send a POST request"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post("http://0.0.0.0:5000/search_user", {'q': q})
    try:
        if req.json():
            print('[{}] {}'.format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print('No result')
    except ValueError as error:
        print('Not a valid JSON')