#!/usr/bin/python3

def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    beg = 0
    for i, c in enumerate(text):
        if i == len(text) - 1:
            print(text[beg:i + 1].strip(), end="")
        elif c in ".?:":
            print(text[beg:i + 1].strip(), end="\n\n")
            beg = i + 1
