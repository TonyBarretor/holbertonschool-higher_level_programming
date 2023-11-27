#!/usr/bin/python3
"""Module that adds arguments to a Python list and saves them to a JSON file."""

import sys
import json
from os import path

def save_to_json_file(my_list, filename):
    """Save a Python list to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_list, file)

def load_from_json_file(filename):
    """Load a Python list from a JSON file."""
    if path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

if __name__ == "__main__":
    # Get the existing list or create an empty list
    my_list = load_from_json_file("add_item.json")

    # Add command line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(my_list, "add_item.json")
