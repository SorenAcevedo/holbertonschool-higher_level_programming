#!/usr/bin/python3
""" Base Tests """
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Tests """
    def test_rectangle_02(self):
        """ Call class with id none """
        r0 = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 10)
        self.assertEqual(r0.height, 2)

        r1 = Rectangle(2, 10, 0, 0, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)

        r2 = Rectangle(2, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 2)

    def test_rectangle_03(self):
        """ Raise Errors """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle("10", "2")
        with self.assertRaises(TypeError):
            Rectangle("10", "2", 0, 0, 10)
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 10)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(ValueError):
            Rectangle(-10, 10)
        with self.assertRaises(ValueError):
            Rectangle(10, -10)

        with self.assertRaises(TypeError):
            Rectangle(10, 10, "a", 1, 98)
        with self.assertRaises(TypeError):
            Rectangle(10, 10, 1, "b", 98)
        with self.assertRaises(ValueError):
            Rectangle(10, 10, -1, 1, 98)
        with self.assertRaises(ValueError):
            Rectangle(10, 10, 1, -1, 98)

    def test_rectangle_04(self):
        """ Area tests """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
        r4 = Rectangle(8, 7, 5, 2, 16)
        self.assertEqual(r4.area(), 56)

    @patch('builtins.print')
    def test_rectangle_05(self, mock_print):
        """ Display """
        Rectangle(2, 3).display()
        d0 = "##\n" * 3
        mock_print.assert_called_with(d0[:-1])

        Rectangle(4, 6).display()
        d0 = "####\n" * 6
        mock_print.assert_called_with(d0[:-1])

    def test_rectangle_06(self):
        """ str """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    @patch('builtins.print')
    def test_rectangle_07(self, mock_print):
        """ Display with x and y """
        Rectangle(2, 3, 2, 2).display()
        d0 = "\n\n" + "  ##\n" * 3
        mock_print.assert_called_with(d0[:-1])

        Rectangle(3, 2, 1, 0).display()
        d0 = " ###\n" * 2
        mock_print.assert_called_with(d0[:-1])

    def test_rectangle_08(self):
        """ Update """
        r1 = Rectangle(1, 1, 1, 1)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/1 - 1/1")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/1 - 2/1")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/1 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/1 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_09(self):
        """ Update with dict """
        r1 = Rectangle(1, 1, 1, 1)
        r1.update(height=5, id=20)
        self.assertEqual(str(r1), "[Rectangle] (20) 1/1 - 1/5")
        r1.update(width=6, x=2)
        self.assertEqual(str(r1), "[Rectangle] (20) 2/1 - 6/5")
        r1.update(y=2, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/2 - 2/5")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
        with self.assertRaises(TypeError):
            r1.update(x=1, height=2, y=3, width="4")

    def test_rectangle_13(self):
        """ Update with dictionary test """
        r1 = Rectangle(10, 2, 1, 9, 10)
        r1d = r1.to_dictionary()
        d = {'id': 10, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1d, d)

        r2 = Rectangle(1, 1)
        r2.update(**r1d)
        self.assertEqual(str(r2), "[Rectangle] (10) 1/9 - 10/2")
        self.assertNotEqual(r1, r2)

if __name__ == '__main__':
        unittest.main()
