#!/usr/bin/python3
""" JSON """
import json


def load_from_json_file(filename):
    """ JSON CONVERTION """
    with open(filename) as f:
        return json.load(f)
