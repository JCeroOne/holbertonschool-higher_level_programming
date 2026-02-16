#!/usr/bin/python3
"""Defines the save_to_json_file function."""

import json


def to_json_string(my_obj, filename):
    """Converts the object to a JSON string and saves it to a file.

    Parameters:
        my_obj: The object to convert.
        filename: The file to save the JSON in."""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
