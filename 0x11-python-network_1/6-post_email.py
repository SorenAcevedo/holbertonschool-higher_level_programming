#!/usr/bin/python3
""" This module fetches url """
import requests
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    r = requests.get(sys.argv[1], values)
    print(r.text)
