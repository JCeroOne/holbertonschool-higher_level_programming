#!/usr/bin/python3
"""Defines the load_from_json_file function."""

import json


def load_from_json_file(filename):
    """Loads a JSON string from a file and converts it to an object.

    Parameters:
        filename: The file to read from.

    Returns: The converted object."""

    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
