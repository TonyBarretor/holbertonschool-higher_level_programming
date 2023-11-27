#!/usr/bin/python3
"""
is_kind_of_class checks if an object is an instance of, 
or if the object is an instance
of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, 
    or if the object is an instance
    of a class that inherited from, the specified class; otherwise False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    bool: True if obj is an instance of a_class or its subclasses; otherwise False.
    """
    return isinstance(obj, a_class)
