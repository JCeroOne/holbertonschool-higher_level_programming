#!/usr/bin/python3
"""Uses the pickle module to serialize and deserialize data."""

import pickle


class CustomObject:
    """A custom object."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the object in a readable format."""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes and saves the object to the specified file.

        Parameters:
            filename: The file to save the data to."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an instance of the class from the specified file.

        Parameters:
            filename: The file to read the data from.

        Returns: An instance of the class with the loadeddata attributes."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (
                FileNotFoundError, 
                EOFError, 
                pickle.UnpicklingError, 
                Exception
            ):
            return None
