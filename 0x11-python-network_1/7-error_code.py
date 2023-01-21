#!/usr/bin/python3
"""Hande HTTPError using requests library
"""
import requests
import sys


def main(url,):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except Exception as e:
        print('Error code: {}'.format(response.status_code))


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
