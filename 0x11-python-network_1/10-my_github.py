#!/usr/bin/python3
""" GitHub Api """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    r_json = r.json()
    print(r_json.get('id'))
