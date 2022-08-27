#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list(my_list)
    if idx < 0 or idx >= len(new):
        return new
    new[idx] = element
    return new
