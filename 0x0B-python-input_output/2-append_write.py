#!/usr/bin/python3
""" Append Write in a File """


def append_write(filename="", text=""):
    """ Append Write in a file function """

    with open(filename, 'a') as f:
        a = f.write(text)
    return a
