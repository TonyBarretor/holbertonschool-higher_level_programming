#!/usr/bin/python3
"""Module for converting an object to its JSON representation (string)"""

import json

def to_json_string(my_obj):
    """
    Converts an object to its JSON representation (string).

    Args:
        my_obj: The object to be converted.
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    to_json_string()
