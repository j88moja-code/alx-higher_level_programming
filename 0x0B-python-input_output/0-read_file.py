#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ Reads and print to
    stdout
    """
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
