#!/usr/bin/python3

def print_square(size):
    """ Prints a square with a size
    checks if "size" is an int
    checks if "size" is a float and less than 0
    checks if "size" is less than 0
    checks if "size" is equal to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
