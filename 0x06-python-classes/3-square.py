#!/usr/bin/python3


class Square:
    """ Class Square """
    def __init__(self, __size=0):
        """ Initializated method
        Args:
            __size (int): Size of square.
        Attributes:
            __size (int): Size of square.
        """
        if type(__size) != int:
            raise TypeError('size must be an integer')
        if __size < 0:
            raise ValueError('size must be >= 0')
        self.__size = __size

    def area(self):
        """ Area public method """
        return self.__size ** 2
