#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        if not matrix:
            return

        for row in matrix:
            for i, num in enumerate(row):
                print("{:d}".format(num), end=" ")
                if i != len(row) - 1:
                    print(" ", end=" ")
            print()

if _name_ == "_main_":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
