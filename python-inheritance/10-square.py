#!/usr/bin/python3
"""
Defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inherits from Rectangle.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        str: The square description in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
