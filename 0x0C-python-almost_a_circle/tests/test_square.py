#!/usr/bin/python3
""" Base Tests """
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ Tests """

    def test_square_10_area(self):
        """ Square test with area """
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    @patch('builtins.print')
    def test_square_10_display(self, mock_print):
        """ Display with x and y """
        Square(5).display()
        d0 = "#####\n" * 5
        mock_print.assert_called_with(d0[:-1])

        Square(2, 2).display()
        d0 = "  ##\n" * 2
        mock_print.assert_called_with(d0[:-1])

        Square(3, 1, 3).display()
        d0 = "\n\n\n" + " ###\n" * 3
        mock_print.assert_called_with(d0[:-1])

    def test_square_11(self):
        """ Call class square """
        s0 = Square(10, 0, 0, 7)
        self.assertEqual(s0.id, 7)
        self.assertEqual(s0.width, 10)
        self.assertEqual(s0.height, 10)
        self.assertEqual(s0.size, 10)

        s1 = Square(5, 0, 0, 8)
        self.assertEqual(s1.id, 8)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 5, 0, 9)
        self.assertEqual(s2.id, 9)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.y, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -1)

    def test_square_12(self):
        """ Square update test """
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_14(self):
        """ Update with dictionary test """
        s1 = Square(10, 2, 1, 9)
        s1d = s1.to_dictionary()
        d = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s1d, d)

        s2 = Square(1, 1)
        s2.update(**s1d)
        self.assertEqual(str(s2), "[Square] (9) 2/1 - 10")
        self.assertNotEqual(s1, s2)

if __name__ == '__main__':
        unittest.main()
