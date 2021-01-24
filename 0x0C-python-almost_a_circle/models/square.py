#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Rectangle Base """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializated method """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y

    @property
    def size(self):
        """ Method to retrieve height """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set height """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__size = value

    def update(self, *args, **kwargs):
        """ update method """
        order = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, order[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Return dictionary method """
        attr = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attr}

    def __str__(self):
        """ str method """
        s = self.size
        x = self.x
        y = self.y
        i = self.id
        return "[Square] ({}) {}/{} - {}".format(i, x, y, s)
