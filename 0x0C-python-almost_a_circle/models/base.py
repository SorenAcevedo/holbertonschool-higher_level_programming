#!/usr/bin/python3
""" Base Class """
import json


class Base():
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializated Method """
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ To json method """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ From json method """
        if json_string:
            return json.loads(json_string)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save Json method """
        filename = cls.__name__ + ".json"
        if list_objs:
            l = cls.to_json_string([i.to_dictionary() for i in list_objs])
        else:
            l = "[]"
        with open(filename, 'w') as fp:
            fp.write(l)

    @classmethod
    def create(cls, **dictionary):
        """ Create instance from dict method """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load from file method """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as fp:
                r = fp.read()
                l = cls.from_json_string(r)
                return [cls.create(**i) for i in l]
        except FileNotFoundError:
            return []
