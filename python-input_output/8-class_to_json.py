#!/usr/bin/python3
"""Defines the class_to_json function."""


def class_to_json(obj):
    """Returns a simplified version of the object, for JSON conversion.

    Parameters:
        obj: The object to convert.

    Returns: The simplified version of the object."""
    return obj.__dict__.copy()
