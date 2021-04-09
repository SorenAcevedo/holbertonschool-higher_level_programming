#!/usr/bin/python3
""" This module fetches url """
import urllib.request
import sys

if len(sys.argv) == 2:
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.headers
        print(html['X-Request-Id'])
