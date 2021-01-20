#!/usr/bin/python3
""" JSON """
import json


def save_to_json_file(my_obj, filename):
    """ JSON CONVERTION """
    js = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(js)
