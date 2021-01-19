#!/usr/bin/python3
""" Class inverted """


class MyInt(int):
    """ Class my int """

    def __eq__(self, value):
        """ equivalent not is equivalent """
        return self.real = value

    def __ne__(self, value):
        """ different not is different """
        return self.real == value
