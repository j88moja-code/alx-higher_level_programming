#!/usr/bin/python3
""" Module for a new Class inherited from int
"""


class MyInt(int):
    """ New subclass of int with new functionalities
    """
    def __eq__(self, other):
        """ inverted == method
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ override of __ne__ (!=) method to the oposite meaning
        """
        return not self.__eq__(other)
