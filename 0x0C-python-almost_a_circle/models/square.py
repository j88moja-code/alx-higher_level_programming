#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init magic method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str magic method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """to_dictionary method"""
        rdict = {}
        rdict["id"] = self.id
        rdict["size"] = self.size
        rdict["x"] = self.x
        rdict["y"] = self.y
        return rdict
