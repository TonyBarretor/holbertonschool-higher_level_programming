#!/usr/bin/python3
"""
function lookup that returns a list of available attributes and methods.
"""


def lookup(obj):
    """
    Returns list names of attributes and methods of an object.
    """
    return dir(obj)
