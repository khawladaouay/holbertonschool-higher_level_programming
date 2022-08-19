#!/usr/bin/python3
"""
script that fetches url"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as f:
        data = f.read()
        print("Body response:")
        print("- type: {}".format(type(data)))
        print("- content: {}".format(data))
        print("- utf8 content: {}".format(data.decode('utf8')))
