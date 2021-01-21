#!/usr/bin/python3
""" Student Class """


class Student():
    """ Class student """
    def __init__(self, first_name, last_name, age):
        """ Initializated Method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ convert to json """
        if type(attrs) == list and all([type(i) == str for i in attrs]):
            dic = {}
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return dic
        return self.__dict__
