#!/usr/bin/python3

"""MyList - Provides a single method."""

class MyList(list):
    
    def print_sorted(self):
        """print_sorted - Prints the list, sorted in ascending order."""

        print(self.sort())
