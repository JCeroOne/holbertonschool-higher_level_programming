#!/usr/bin/python3
"""Defines functions to serialize and deserialize data."""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes the data and saves it to the specified file.

    Parameters:
        data: The data to serialize.
        filename: The file to save the data to."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    """Reads and deserializes data saved within a file.

    Parameters:
        filename: The file to read the data from.

    Returns: The deserialized data."""
    d = None
    with open(filename, "r", encoding="utf-8"):
        d = f.read()
    return json.loads(d)
