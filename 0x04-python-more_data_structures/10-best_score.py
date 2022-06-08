#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    ch = 0
    for i in a_dictionary:
        if a_dictionary[i] is None:
            return None
        if ch == 0:
            high = a_dictionary[i]
        if a_dictionary[i] > high:
            high = a_dictionary[i]
        ch += 1

    for x in a_dictionary:
        if a_dictionary[x] == high:
            return x
