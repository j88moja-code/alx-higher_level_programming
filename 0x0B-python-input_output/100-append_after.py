#!/usr/bin/python3
"""Function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text to the file
    """
    res_string = ""

    with open(filename, encoding='UTF-8') as f:

        for line in f:
            res_string += line
            if search_string in line:
                res_string += new_string

    with open(filename, encoding='UTF-8', mode="w") as f:
        f.write(res_string)
