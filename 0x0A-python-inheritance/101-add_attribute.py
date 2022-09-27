#!/usr/bin/python3
""" Function that adds a new attribute to an object if its possible
"""


def add_attribute(obj, name, value):
    """ The obj is evaluated before creating the new -name- attribute,
    with -value-
     Args:
        obj (any type)
        name (string)
        value (any type): value to the new attribute
    """
    methods = list(dir(obj))
    if "__dict__" not in methods:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
