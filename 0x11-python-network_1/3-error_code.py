#!/usr/bin/python3
""" This module consider an error in the request """
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read())

    except urllib.error.URLError as e:
        print('Error Code: {}'.format(e.code))
