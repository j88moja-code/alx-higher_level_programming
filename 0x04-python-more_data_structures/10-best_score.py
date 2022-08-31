#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    ret = list(a_dictionary.keys())[0]
    test = a_dictionary[ret]
    for i, j in a_dictionary.items():
        if j > test:
            test = j
            ret = i
    return (ret)
