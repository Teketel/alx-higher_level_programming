#!/usr/bin/python3
"""Fetch URL using requests library
"""
import requests


def main(url,):
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    main(url)
