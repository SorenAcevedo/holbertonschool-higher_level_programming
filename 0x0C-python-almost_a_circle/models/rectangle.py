#!/usr/bin/python3
""" Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializated method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ Method to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method to set height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
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
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """ Method to retrieve x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Method to set x """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Method to retrieve y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Method to set y """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Method to obtain area """
        return self.__width * self.__height

    def display(self):
        """ Method to display Rectangle """
        h = self.height
        w = self.width
        x = self.x
        print("{}".format('\n' * self.y), end="")
        print("".join([' ' * x + '#' * w + '\n' for i in range(h)])[:-1])

    def update(self, *args, **kwargs):
        """ update method """
        order = ["width", "height", "x", "y"]
        if args and len(args) > 0:
            super().__init__(args[0])
            for i, arg in enumerate(args[1:]):
                setattr(self, order[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ Return dictionary method """
        attr = ["id", "width", "height", "x", "y"]
        return {k: getattr(self, k) for k in attr}

    def __str__(self):
        """ str method """
        h = self.height
        w = self.width
        x = self.x
        y = self.y
        i = self.id
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)
