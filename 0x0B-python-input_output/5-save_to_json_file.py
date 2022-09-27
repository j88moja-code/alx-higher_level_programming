#!/usr/bin/python3
"""Function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a string containing the object in json format
    """
    with open(filename, encoding='UTF-8', mode="w") as f:
        string = json.dumps(my_obj)
        f.write(string)
