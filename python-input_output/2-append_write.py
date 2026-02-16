#!/usr/bin/python3

"""Defines the append_write function."""


def append_write(filename="", text=""):
    """Adds the given text to the end of the file, creates it if needed.

    Parameters:
        filename: The file to append to, or create.
        text: The text to append to the file.

    Returns: The number of characters written to the file."""
    
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
