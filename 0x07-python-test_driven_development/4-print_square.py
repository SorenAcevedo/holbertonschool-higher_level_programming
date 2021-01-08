#!/usr/bin/python3
"""
Print Square
"""


def print_square(size):
    """ Print Square """

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("{}".format("#" * size))
