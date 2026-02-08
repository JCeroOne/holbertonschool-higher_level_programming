#!/usr/bin/python3
"""Provides the 'is_same_class' function."""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of the provided class.
    Parameters:
        obj - The object to check
        a_class - The class to compare the object to

    Returns:
        True if the object is an instance of the class
        False otherwise"""
    return type(obj) is a_class
