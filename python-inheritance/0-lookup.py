
#!/usr/bin/python3

"""Provides a lookup function, which lists the methods and attributes of an object"""

def lookup(obj):
    return obj.__dict__.keys()
