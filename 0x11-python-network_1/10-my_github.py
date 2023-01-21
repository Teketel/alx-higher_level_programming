#!/usr/bin/python3
"""Get user Github ID from Github API using requests library
"""
import requests
import sys


def main(url, user, token):
    headers = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=headers)
    print(response.json().get('id'))


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    token = sys.argv[2]
    main(url, user, token)
