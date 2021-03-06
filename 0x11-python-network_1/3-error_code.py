#!/usr/bin/python3
""" This module consider an error in the request """
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
