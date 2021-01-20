#!/usr/bin/python3
""" Write in a File """


def write_file(filename="", text=""):
    """ Write in a file function """

    with open(filename, 'w') as f:
        a = f.write(text)
    return a
