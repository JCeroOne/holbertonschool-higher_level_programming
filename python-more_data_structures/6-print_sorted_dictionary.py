#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if type(a_dictionary) is not dict:
        return
    k = sorted(a_dictionary.keys())
    for el in k:
        print("{}: {}".format(el, a_dictionary[el]))
