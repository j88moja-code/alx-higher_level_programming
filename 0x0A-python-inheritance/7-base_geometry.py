#!/usr/bin/python3
""" Class BaseGeometry
"""


class BaseGeometry:
    """ New class"""
    def integer_validator(self, name, value):
        """ Checks and validates the values"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")

    def area(self):
        """ Raises an error
        """
        raise Exception("area() is not implemented")
