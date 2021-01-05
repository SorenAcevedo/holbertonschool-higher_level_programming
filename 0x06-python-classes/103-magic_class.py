#!/usr/bin/python3
"""
Bytecode Class
"""
import math


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

        return math.pi * self.__radius ** 2

    def circumference(self):
        """ Circumference method """

        return 2 * math.pi * self.__radius
