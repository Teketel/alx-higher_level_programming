#!/usr/bin/python3
"""Get user Github ID from Github API using requests library
"""
import requests
import sys


def main(url,):

    response = requests.get(url)
    response = response.json()
    for commit in response:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))


if __name__ == '__main__':
    repo_name = sys.argv[1]
    user_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
        user_name, repo_name)
    main(url,)
