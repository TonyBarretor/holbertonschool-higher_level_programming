#!/usr/bin/python3
"""Module to define the Student class."""

class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        json_dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__"):
                json_dict[key] = value
        return json_dict
