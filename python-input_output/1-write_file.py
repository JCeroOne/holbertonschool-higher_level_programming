#!/usr/bin/python3

"""Defines the write_file function."""


def write_file(filename="", text=""):
    """Creates or overwrites the specified file with the given text.

    Parameters:
        filename: The file to create or overwrite.
        text: The text to write to the file.

    Returns: The number of characters written."""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
