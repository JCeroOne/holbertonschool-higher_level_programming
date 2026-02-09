#!/usr/bin/python3
"""Provides the 'is_kind_of_class' function."""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a subclass of the provided class.
    Parameters:
        obj - The object to check
        a_class - The class to compare the object to

    Returns:
        True if the object is an instance of a subclass
        False otherwise"""
    return isinstance(obj, a_class) and type(obj) is not a_class
