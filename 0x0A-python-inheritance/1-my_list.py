#!/usr/bin/python3
""" Module that contains a class that inherits from list
"""


class MyList(list):
    """ New class MyList that inherits from list
    """
    def print_sorted(self):
        """ Prints the list sorted
        """
        new_list = sorted(self)
        print(new_list)
        return new_list
