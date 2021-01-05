#!/usr/bin/python3
"""
Bytecode Class
"""


class MagicClass():
    """ MagicClass """
    def __init__(self, radius):
        """ Initialized method.
        Args:
            radius (int or float): radius of circle.
        Attribute:
            __radius (int or float): radius or circle.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
        return None

    def area(self):
        """ Area method """
        from math import pi

        return pi * self.__radius ** 2

    def circumference(self):
        """ Circumference method """
        from math import pi

        return 2 * pi * self.__radius
