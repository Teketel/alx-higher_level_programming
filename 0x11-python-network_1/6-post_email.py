#!/usr/bin/python3
"""Post request using requests library
"""
import requests
import sys


def main(url, email):
    response = requests.post(url,
                             data={'email': email})
    print(response.text)


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
