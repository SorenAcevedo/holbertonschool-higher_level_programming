#!/usr/bin/python3
""" Insert attr """


def add_attribute(obj, name, value):
    """ Add attr method """

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
