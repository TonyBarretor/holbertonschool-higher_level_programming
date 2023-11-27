#!/usr/bin/python3
"""
Defines the BaseGeometry class with public instance methods 
area() and integer_validator().
"""


class BaseGeometry:
    """
    A class representing the base geometry.

    Methods:
    - area(): Raises an Exception with the message 
    "area() is not implemented."
    - integer_validator(name, value): Validates the value.

    Attributes:
    - name (str): The name of the value being validated.
    - value: The value to be validated.
    """

    def area(self):
        """
        Raises an Exception with the message 
        "area() is not implemented."

        Raises:
        Exception: Always raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Parameters:
        - name (str): The name of the value being validated.
        - value: The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
