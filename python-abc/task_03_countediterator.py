#!/usr/bin/python3
"""CountedIterator class."""


class CountedIterator:
    """Extends the built-in iterator function."""

    def __init__(self, iterable):
        self.__iter = iter(iterable)
        self.__count = 0

    def get_count(self):
        return self.__count

    def __next__(self):
        item = next(self.__iter)
        self.__count += 1
        return item
