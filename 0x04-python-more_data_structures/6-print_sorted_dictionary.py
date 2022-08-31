#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for akey in sorted([key for key in a_dictionary]):
        print("{}: {}".format(akey, a_dictionary[akey]))
