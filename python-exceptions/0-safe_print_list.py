#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            printed = i + 1
        print()
        return printed
    except:
        print()
        return printed
