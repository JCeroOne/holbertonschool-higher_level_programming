#!/usr/bin/python3
"""Defines the print_square function."""


def print_square(size):
    """Prints a square to the console.

    Parameters:
        size (int): The size of the square.
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print('#', end='')

            if j % size == 0 and j > 0:
                print()
