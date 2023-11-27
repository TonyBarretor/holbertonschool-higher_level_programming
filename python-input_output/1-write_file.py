#!/usr/bin/python3
"""Module for writing a string to a text file (UTF8)"""

def write_file(filename="", text=""):
    """
    Returns the number of characters written.

    Args:
        filename (str): The name of the text file.
        text (str): The string to be written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters


if __name__ == "__main__":
    write_file()
