#!/usr/bin/python3
"""Provides the 'BaseGeometry' and 'Rectangle' classes."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a Rectangle in Python."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
