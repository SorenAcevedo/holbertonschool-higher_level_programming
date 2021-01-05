#!/usr/bin/python3


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Initializated method
        Args:
            size (int): Size of square.
        Attributes:
            __size (int): Size of square.
        """

        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

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

    def area(self):
        """ Area public method """

        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        return self.__size ** 2
