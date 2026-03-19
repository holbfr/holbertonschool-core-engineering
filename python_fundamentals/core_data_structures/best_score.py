#!/usr/bin/env python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max = ()
    for k, v in a_dictionary.items():
        if len(max) == 0:
            max = (k, v)
        elif v > max[1]:
            max = (k, v)
    return max[0]
