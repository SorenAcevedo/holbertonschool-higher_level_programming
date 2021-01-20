#!/usr/bin/python3
""" Class to Json """
import json


def class_to_json(obj):
    """ class to json """
    return json.dumps(obj.__dict__)
