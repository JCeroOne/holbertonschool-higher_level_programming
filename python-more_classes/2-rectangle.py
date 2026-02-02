#!/usr/bin/python3


"""Defines a Rectangle class, with private width and height attributes, and methods to calculate area and perimeter."""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        return (2 * self.__width + 2 * self.__height) if (self.__width > 0 and self.__height > 0) else 0
