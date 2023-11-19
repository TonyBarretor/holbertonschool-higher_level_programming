#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element of two lists and returns a new list with all divisions.
    """
    result = []

    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError):
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                print("division by 0")
                division = 0
            elif not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                division = 0
            else:
                print("out of range")
                division = 0
        finally:
            result.append(division)

    return result
