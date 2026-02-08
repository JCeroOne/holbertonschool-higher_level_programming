#!/usr/bin/python3

"""MyList - Provides a single method."""

class MyList(list):
    """MyList - A class that expands the built-in list class."""
    
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """print_sorted - Prints the list, sorted in ascending order."""

        print(self.sort())
