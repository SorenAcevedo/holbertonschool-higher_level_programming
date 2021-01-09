#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class with test """
    def test_max(self):
        """Tests"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([7, 5, 3]), 7)
        self.assertEqual(max_integer([1, 5, 3]), 5)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
