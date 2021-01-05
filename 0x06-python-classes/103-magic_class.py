#!/usr/bin/python3
"""
Bytecode Class
"""


class MagicClass():

    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
        return None

    def area(self):
        from math import pi

        return pi * self.__radius ** 2

    def circumference(self):
        from math import pi

        return 2 * pi * self.__radius
