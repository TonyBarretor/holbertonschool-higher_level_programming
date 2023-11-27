#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.
    """
    json_dict = obj.__dict__.copy()
    json_dict["__class__"] = obj.__class__.__name__
    return json_dict
