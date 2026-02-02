#!/usr/bin/python3

"""Define a square class with a private, instance attribute named size.
'size' must be an integer, and greater or equal to 0. Now the size can actually be modified, so I guess that may be kind of useful."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all((type(i) is int and i >= 0) for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square to the console."""
        if self.__size == 0:
            print()
        print("\n" * self.__position[1] + (" " * self.__position[0] + "#" * self.__size + "\n") * self.__size, end="")

