#!/usr/bin/python3
""" This module fetches url """
import requests
import sys

if __name__ == "__main__":
    values = {'q': ''}
    if len(sys.argv) == 2:
        values['q'] = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=values)
    try:
        r_json = r.json()
        if r_json:
            print('[{}] {}'.format(r_json.get('id'), r_json.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
