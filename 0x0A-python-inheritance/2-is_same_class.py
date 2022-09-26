#!/usr/bin/python3
""" Module with a function that returns True if the object is an instance
"""


def is_same_class(obj, a_class):
    """ Checks if obj is an instance of a_class
    """
    return type(obj) is a_class
