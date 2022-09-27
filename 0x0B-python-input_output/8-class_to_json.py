#!/usr/bin/python3
"""Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """Serializes with Dict method of the object
    """
    if obj.__dict__:
        return obj.__dict__
