#!/usr/bin/python3

"""Function that add two integers a and b"""


def add_integer(a, b=98):
    """ Return addition of a and b
    raise TypeError:
        if a and b are not integers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
