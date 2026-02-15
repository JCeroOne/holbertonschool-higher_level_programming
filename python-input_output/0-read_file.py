#!/usr/bin/python3

"""Defines the read_file function."""


def read_file(filename=""):
    """Reads a file and prints its contents to the console.

    Parameters:
        filename: The name of the file to read."""

    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
