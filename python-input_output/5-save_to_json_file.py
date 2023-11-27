#!/usr/bin/python3
"""Module for writing an object to a text file using a JSON"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    save_to_json_file()
