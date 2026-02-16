#!/usr/bin/python3
"""Defines the to_json_string function."""

import json

def to_json_string(my_obj):
    """Converts the object to a JSON string.

    Parameters:
        my_obj: The object to convert.

    Returns: A JSON representation of the object."""
    return json.dumps(my_obj)
