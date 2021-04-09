#!/usr/bin/python3
""" This module fetches url """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html.decode('utf-8'))))
        print('\t- content: {}'.format(html.decode('utf-8')))
