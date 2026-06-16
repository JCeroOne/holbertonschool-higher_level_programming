#!/usr/bin/python3
"""
Defines add_integer, a function that adds two integers together.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Parameters:
        a (int): The first integer
        b (int): The second integer

    Returns:
        (int) The addition result.
    """

    if type(a) is float:
        a = int(a)
    else if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    else if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
