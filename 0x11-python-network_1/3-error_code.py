#!/usr/bin/python3
""" This module consider an error in the request """
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            print(response.read())

    except urllib.error.URLError as e:
        print(e.reason)
