#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

"""Abstract class 'Shape' and implementations."""


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius=1):
        self.__radius = radius

    def area(self):
        return math.pi * math.pow(self.__radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):

    def __init__(self, width=1, height=1):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * self.__width + 2 * self.__height


def shape_info(obj):
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
