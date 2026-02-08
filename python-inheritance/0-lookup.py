
#!/usr/bin/python3

"""Provides a lookup function, which lists the methods and attributes of an object"""

def lookup(obj):
    """
    Parameters:
        obj - The object from which to get methods and attributes

    Returns: A list containing the methods and attributes of the object
    """
    return dir(obj)
