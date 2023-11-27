#!/usr/bin/python3
"""
Defines the BaseGeometry class with a public instance method area().
"""


class BaseGeometry:
    """
    A class representing the base geometry.

    Methods:
    - area(): Raises an Exception with the message "area() is not implemented."
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."

        Raises:
        Exception: Always raises an Exception.
        """
        raise Exception("area() is not implemented")
