#!/usr/bin/python3

def pow(a, b):
    """
    Computes the value of a to the power of b.

    Args:
    - a: base
    - b: exponent

    Returns:
    - The value of a ^ b
    """
    result = 1

    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(abs(b)):
            result /= a

    return result
