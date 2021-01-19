#!/usr/bin/python3
""" Class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size):
        """ Initializated method """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
