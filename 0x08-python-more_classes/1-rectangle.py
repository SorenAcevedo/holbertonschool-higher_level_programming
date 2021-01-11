#!/usr/bin/python3
"""
This module have de Rectangle Class
"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializated method """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Method to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method to set height """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    @property
    def width(self):
        """ Method to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method to set width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value