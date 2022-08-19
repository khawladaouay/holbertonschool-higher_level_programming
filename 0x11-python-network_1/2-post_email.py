#!/usr/bin/python3
""""sends a POST request to the passed URL with the email """
from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as f:
        page = f.read()
        print(page.decode('utf-8'))
