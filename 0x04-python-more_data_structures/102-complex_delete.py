#!/usr/bin/python
def complex_delete(a_dictionary, value):
    s = a_dictionary.copy()
    for k, v in s.items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
