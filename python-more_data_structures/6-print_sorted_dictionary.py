#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for el in k:
        print("{}: {}".format(el, a_dictionary[el]))
