#!/usr/bin/python3
"""
func is_same_class checks if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is instance of the specified class,else False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
