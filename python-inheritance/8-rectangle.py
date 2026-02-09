#!/usr/bin/python3
"""Provides the 'BaseGeometry' and 'Rectangle' classes."""


class BaseGeometry():
    """Apparently, the base of many future subclasses."""

    def area(self):
        """Will calculate the area of the geometry in subclasses."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether <name> is a positive integer.
        Parameters:
            name - The name of the numeric value
            value - The value of <name>"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a Rectangle in Python."""

    def __init__(self, width, height):
        self.__width = super.integer_validator("width", width)
        self.__height = super.integer_validator("height", height)
