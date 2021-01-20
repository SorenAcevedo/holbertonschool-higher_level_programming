#!/usr/bin/python3
""" Student Class """


class Student():
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ Initializated Method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ convert to json """
        return self.__dict__
