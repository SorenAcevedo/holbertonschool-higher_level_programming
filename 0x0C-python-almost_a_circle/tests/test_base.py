#!/usr/bin/python3
""" Base Tests """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ Tests """
    def test_base_01(self):
        """ Call class with id none """
        b0 = Base()
        b1 = Base(12)
        b2 = Base()
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 2)

    def test_base_15(self):
        """ Dictionary to JSON tests"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        jd = Base.to_json_string([dictionary])
        jd0 = '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(jd, jd0)
        self.assertEqual(type(jd), type(jd0))

    def test_base_16(self):
        """ JSON to file """
        r1 = Rectangle(10, 7, 2, 8, 90)
        r2 = Rectangle(2, 4, 0, 0, 91)
        a = '[{"id": 90, "width": 10, "height": 7, "x": 2, "y": 8}'
        b = ', {"id": 91, "width": 2, "height": 4, "x": 0, "y": 0}]'
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            f = file.read()
        self.assertEqual(f, a + b)

    def test_base_17(self):
        """ JSON to Dict """
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string([]))

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        jli = Rectangle.to_json_string(list_input)
        a = '[{"id": 89, "width": 10, "height": 4, "x": 0, "y": 0}'
        b = ', {"id": 7, "width": 1, "height": 7, "x": 0, "y": 0}]'
        self.assertEqual(str, type(jli))

    def test_base_18(self):
        """ Dict instance """
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertNotEqual(r1, r2)

    def test_base_19(self):
        """ Load from file test """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        ll = Rectangle.load_from_file()
        for i, rect in enumerate(ll):
            self.assertEqual(str(rect), str(l[i]))

if __name__ == '__main__':
        unittest.main()
