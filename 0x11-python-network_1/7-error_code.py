#!/usr/bin/python3
""" This module fetches url """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
