#!/usr/bin/python3
"""ERROR"""
import requests
from sys import argv

if __name__ == "__main__":
    data = requests.get(argv[1])
    if(data.status_code >= 400):
        print("Error code: {}".format(data.status_code))
    else:
        print(data.text)
