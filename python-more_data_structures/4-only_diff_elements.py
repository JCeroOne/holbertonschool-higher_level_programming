#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    s = set()
    for el in set_1:
        if el not in set_2:
            s.add(el)
    for el in set_2:
        if el not in set_1:
            s.add(el)
    return s
