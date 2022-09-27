#!/usr/bin/python3
"""Function that creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """ Reads a file and returns an object
    """
    with open(filename, encoding='UTF-8') as f:
        file_cont = f.read()
        return json.loads(file_cont)
