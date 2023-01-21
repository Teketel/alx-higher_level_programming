#!/usr/bin/python3
"""POST data and parse JSON response using requests library
"""
import requests
import sys


def main(url, q):
    response = requests.post(url, data={'q': q})
    try:
        response_json = response.json()

        if not response_json:
            print('No result')
        else:
            print('[{}] {}'.format(response_json.get(
                'id'), response_json.get('name')))

    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ''
    main(url, q)
