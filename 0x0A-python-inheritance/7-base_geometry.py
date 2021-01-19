#!/usr/bin/python3
""" Empty class """


class BaseGeometry():
    """ Class BaseGeometry """

    def area(self):
        """ Area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate value """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} must be greater than 0'.format(name))
