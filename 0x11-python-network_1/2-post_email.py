#!/usr/bin/python3
""" This module fetches url """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        values = {'email': sys.argv[2]}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        with urllib.request.urlopen(url, data) as response:
            print(response.read())
