#!/usr/bin/python3
""""ERRor """
from sys import argv
import urllib.request
import urllib.error
if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as f:
        print("Error code: {}".format(f.code))
