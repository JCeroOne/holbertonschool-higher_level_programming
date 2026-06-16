#!/usr/bin/python3
"""Defines the say_my_name function.
"""


def say_my_name(first_name, last_name=''):
    """Prints the first name and last name.

    Parameters:
        first_name (string): The first name.
        last_name (string): The last name.
    """

    fnExc = "first_name must be a string"
    lnExc = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(fnExc)
    if type(last_name) != str:
        raise TypeError(lnExc)

    print("My name is {}".format(first_name), end='')
    if len(last_name) == 0:
        print()
    else:
        print(" {}".format(last_name))