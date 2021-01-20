#!/usr/bin/python3
""" Load, add, save """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    l = load_from_json_file("add_item.json")
except:
    l = []
l.extend(sys.argv[1:])
save_to_json_file(l, "add_item.json")
