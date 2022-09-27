#!/usr/bin/python3
"""Returns a list of lists of integers representing the Pascals triangle of n
"""


def pascal_triangle(n):
    """Returns a list of list with pascal numbers
    """
    triangle = []
    if n <= 0:
        return triangle

    triangle.append([1])
    if n == 1:
        return triangle

    old_row = [1, 1]
    triangle.append(old_row)
    if n == 2:
        return triangle

    for lines in range(3, n + 1):

        new_row = []
        new_row.append(1)
        for values in range(1, lines - 1):
            new_row.append(old_row[values] + old_row[values - 1])
        new_row.append(1)
        triangle.append(new_row)
        old_row = new_row

    return triangle
