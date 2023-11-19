#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    # Print the formatted message
    print("My name is {} {}".format(first_name, last_name))

# Uncomment the lines below if you want to test the function interactively
# say_my_name("John", "Smith")
# say_my_name("Walter", "White")
# say_my_name("Bob")
# say_my_name(12, "White")
