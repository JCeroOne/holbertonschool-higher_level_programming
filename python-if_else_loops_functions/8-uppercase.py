#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    return False

def uppercase(str):
    res = ""
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            res += chr(ord(str[i]) - 32)
        else:
            res += str[i]
    print("{}".format(res))
