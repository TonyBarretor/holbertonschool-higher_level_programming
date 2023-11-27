#!/usr/bin/python3
"""Module to convert class instance to JSON representation."""

def class_to_json(obj):
    """Converts a class instance to a JSON-serializable dictionary."""
    json_dict = {}
    
    # Add all attributes that are not methods or private
    for key, value in obj.__dict__.items():
        if not callable(value) and not key.startswith("__"):
            json_dict[key] = value
    
    return json_dict
