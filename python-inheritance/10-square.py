#!/usr/bin/python3
"""Provides a 'Square' class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square in Python."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def area(self):
        return self.__size * self.__size
