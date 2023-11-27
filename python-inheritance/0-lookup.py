#!/usr/bin/python3
"""
This module defines a function lookup that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list object containing the available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list containing the names of attributes and methods.
    """
    return dir(obj)
