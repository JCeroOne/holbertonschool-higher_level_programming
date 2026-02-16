#!/usr/bin/python3
"""Creates the Student class."""


class Student:
    """A Python representation of a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a simplified, JSON-ready version of the student."""
        if attrs is None:
            return self.__dict__.copy()
        return {k: v for k, v in self.__dict__.items() if k in attrs}
