#!/usr/bin/python3
"""Response header value
"""
import urllib.request
import sys


def main(url):
    with urllib.request.urlopen(url) as response:
        for header in response.getheaders():
            if header[0] == 'X-Request-Id':
                print(header[1])


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
