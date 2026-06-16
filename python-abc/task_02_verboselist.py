#!/usr/bin/python3
"""VerboseList class."""


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        items = list(items)
        super().extend(items)
        print(f"Extended the list with {len(items)} items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        value = super().pop(index)
        print(f"Popped [{value}] from the list.")
        return value
