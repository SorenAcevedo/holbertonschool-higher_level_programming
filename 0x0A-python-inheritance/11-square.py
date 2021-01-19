#!/usr/bin/python3
""" Class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size):
        """ Initializated method """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ str method """
        return "[Square] {}/{}".format(self.__size, self.__size)
