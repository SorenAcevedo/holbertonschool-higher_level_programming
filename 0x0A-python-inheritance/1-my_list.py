#!/usr/bin/python3
""" Class My list """


class MyList(list):
    """ Class Mylist """

    def __init__(self):
        """ Initializated method """
        super().__init__()

    def print_sorted(self):
        """ Print sorted list method """
        print(sorted(self))
