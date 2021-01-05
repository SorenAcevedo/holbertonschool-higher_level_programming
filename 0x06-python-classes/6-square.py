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
        self.size = __size
        self.__size = self.size
        
        if type(self.size) != int:
            raise TypeError('size must be an integer')
        if __size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Area public method
        Args:
            self: isntance
        """
        if type(self.size) != int:
            raise TypeError('size must be an integer')
        return self.size ** 2

    def my_print(self):
        """ Print square public method
            Args:
                self: isntance
        """
        if self.size > 0:
            for i in range(self.size):
                print("#", end="")
        else:
            print()

