#!/usr/bin/python3
"""VerboseList class."""


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, items):
        super().extend(items)
        print(f"Extending the list with {count} items.")

    def remove(self, item):
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            value = super().pop()
            print(f"Popped [{value}] from the list.")
        else:
            value = super().pop(index)
            print(f"Popped [{value}] from the list.")
