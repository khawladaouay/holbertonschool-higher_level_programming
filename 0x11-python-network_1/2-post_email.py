#!/usr/bin/python3
""""sends a POST request to the passed URL with the email """


if __name__ == '__main__':
    from sys import argv
    import urllib.parse
    import urllib.request
    url = argv[1]
    values = argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as f:
        page = f.read()
        print(page.decode('utf-8'))
