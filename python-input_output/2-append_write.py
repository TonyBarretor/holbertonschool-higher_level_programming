#!/usr/bin/python3
"""Module for appending a string to the end of a text file (UTF8)"""

def append_write(filename="", text=""):
    """
    Returns the number of characters added.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be appended to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added

if __name__ == "__main__":
    append_write()
