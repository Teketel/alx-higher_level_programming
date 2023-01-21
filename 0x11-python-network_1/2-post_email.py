#!/usr/bin/python3
"""POST an email
"""
import urllib.request
import urllib.parse
import sys


def main(url, email):
    data = urllib.parse.urlencode({'email': email})
    request = urllib.request.Request(url, data.encode('ascii'))
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
