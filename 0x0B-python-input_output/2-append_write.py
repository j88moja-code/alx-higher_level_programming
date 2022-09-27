#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Function using the mode a
    """
    with open(filename, encoding='UTF-8', mode="a") as f:
        return f.write(text)
