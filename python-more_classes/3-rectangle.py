#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, and perimeter"""


class Rectangle:
    """Rectangle class with width and height attributes"""
    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the rectangle perimeter"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(['#' * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a string representation of the object"""
        return f"Rectangle({self.width}, {self.height})"
