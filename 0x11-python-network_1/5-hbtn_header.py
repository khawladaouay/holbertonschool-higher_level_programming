#!/usr/bin/python3
"""fetches  https://intranet.hbtn.io/status"""
import requests
from sys import argv
if __name__ == "__main__":
    date = requests.get(argv[1])
    print(date.headers.get('X-Request-Id'))
