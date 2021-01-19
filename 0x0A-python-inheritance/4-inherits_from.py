#!/usr/bin/python3
""" Only Sub class of """


def inherits_from(obj, a_class):
    """ Instance sub Class function """
    if obj.__class__ != a_class:
        return issubclass(obj.__class__, a_class)
