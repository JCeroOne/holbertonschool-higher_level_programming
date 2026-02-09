#!/usr/bin/python3
"""Provides the 'BaseGeometry' class."""


class BaseGeometry:
    """A currently empty class."""
    
    def area(self):
        """Will calculate the area of the geometry in subclasses."""
        raise Exception("area() is not implemented")
