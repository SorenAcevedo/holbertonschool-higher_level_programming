#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ Read file function """

    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
