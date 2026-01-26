#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    for k in a_dictionary:
        if a_dictionary[k] > a_dictionary[max_score] or not max_score:
            max_score = k
    return max_score
