#!/usr/bin/python3
"""
This module have de square Class
"""


class Square:
    """ Class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializated method
        Args:
            size (int): Size of square.
            position (int tuple):
        Attributes:
            __size (int): Size of square.
            __position (int tuple): int tuple.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to retrieve size """

        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set new size
        Args:
            self: instance
            value (int): new size
        """

        if type(value) != int:
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """ Method to retrieve position """

        return self.__position

    @position.setter
    def position(self, value):
        """ Method to set new position
        Args:
            value (tuple): new position
        """

        if (type(value) != tuple or
                len(value) != 2 or
                type(value[0]) != int or
                type(value[1]) != int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Area public method """

        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        return self.__size ** 2

    def my_print(self):
        """ Print square method """
        if self.__size < 0:
            print()
            return

        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print("{}".format((" " * self.__position[0] + "#" * self.__size)))
