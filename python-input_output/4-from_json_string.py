#!/usr/bin/python3
"""Module for converting a JSON string to a Python object (data structure)"""

import json

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted.
    """
    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string()
