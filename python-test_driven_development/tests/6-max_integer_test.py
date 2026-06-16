#!/usr/bin/python3
import unittest
"""Tests for the max_integer function."""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Tests if the function returns the expected value."""

        self.assertIsNone(max_integer([]))
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertAlmostEqual(max_integer([-4, -3, -2, -1, 0]), 0)
        self.assertAlmostEqual(max_integer([-90, -120, -150, -180]), -90)
        self.assertAlmostEqual(max_integer([1.0, 1.5, 1.6, 3.7, 2.3]), 3.7)
        self.assertAlmostEqual(max_integer([7.7]), 7.7)

    def test_wrong_types(self):
        """Tests if the function raises the expected exceptions."""

        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["Monty", 89, 34, -9.7, "Python"])
