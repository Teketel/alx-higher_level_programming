#!/usr/bin/python3
"""Parse response header using requests library
"""
import requests
import sys


def main(url,):
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
