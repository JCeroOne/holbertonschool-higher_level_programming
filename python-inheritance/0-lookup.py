#!/usr/bin/python3

"""Lookup - lists the methods and attributes of an object."""


def lookup(obj):
    """Lookup - lists the methods and attributes of an object.
    Parameters:
        obj - The object from which to get methods and attributes

    Returns: A list containing the methods and attributes of the object
    """

    return dir(obj)
