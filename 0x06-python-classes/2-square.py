#!/usr/bin/python3


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ Initialized method
        Args:
            __size (int): Size of square.
        Attributes:
            __size (int): Size of square.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
