#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list using a loop.
    """
    printed_elements = 0

    for i in range(min(x, len(my_list))):
        print("{}".format(my_list[i]), end="")
        printed_elements += 1

    print()
    return printed_elements
