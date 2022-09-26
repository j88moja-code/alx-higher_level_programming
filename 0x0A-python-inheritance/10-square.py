#!/usr/bin/python3
""" Subclass Rectangle
Subclass Square
Class BaseGoemetry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ New Subclass"""
    def __init__(self, size):
        """ Creates a square by using the super() method"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
