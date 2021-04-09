#!/usr/bin/python3
""" This module fetches url """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    response = {'type': type(html), 'content': html,
                'utf8 content': html.decode('utf-8')}
    [print('\t- {}: {}'.format(k, v)) for k, v in response.items()]
