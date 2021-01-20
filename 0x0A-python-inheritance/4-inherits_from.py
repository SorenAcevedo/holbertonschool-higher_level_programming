#!/usr/bin/python3
""" Only Sub class of """


def inherits_from(obj, a_class):
    """ Instance sub Class function """
    return type(obj) != a_class and issubclass(type(obj), a_class)
