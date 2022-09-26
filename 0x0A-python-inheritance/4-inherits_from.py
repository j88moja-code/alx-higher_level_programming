#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ Checks if obj is an instance of subclass of a_class
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
