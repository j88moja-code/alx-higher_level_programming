#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """ Function using the mode w
    """
    with open(filename, encoding='UTF-8', mode="w") as f:
        return f.write(text)
