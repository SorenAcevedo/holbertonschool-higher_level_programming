#!/usr/bin/python3
"""
This module have de Rectangle Class
"""


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializated method """
        self.width = width
        self.height = height

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

    def area(self):
        """ Method to obtain area """
        return self.__width * self.__height

    def perimeter(self):
        """ Method to obtain perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __del__(self):
        """ Method to delete instance """
        print("Bye rectangle...")

    def __str__(self):
        """ Method to represent instance """
        l = self.__height
        if self.__height == 0 or self.__width == 0:
            return ""
        return "".join([('#' * self.__width) + '\n' for i in range(l)])[:-1]

    def __repr__(self):
        """ Method to represent """
        l = self.__height
        return "Rectangle(" + str(self.__width) + ', ' + str(l) + ')'
