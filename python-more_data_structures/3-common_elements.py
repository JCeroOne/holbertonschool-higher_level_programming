#!/usr/bin/python3
def common_elements(set_1, set_2):
    s = set()
    for el in set_1:
        if el in set_2:
            s.add(el)
    return s
