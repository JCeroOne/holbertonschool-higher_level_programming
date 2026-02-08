#!/usr/bin/python3
"""is_same_class - Checks if an object is exactly an instance of a given class."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of the provided class.
    Parameters:
        obj - The object to check
        a_class - The class to compare the object to

    Returns:
        True if the object is an instance of the class
        False otherwise"""
    return isinstance(obj, a_class)
