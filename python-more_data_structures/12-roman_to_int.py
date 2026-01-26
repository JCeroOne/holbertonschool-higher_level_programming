#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and nums[roman_string[i + 1]] > nums[roman_string[i]]:
            res += nums[roman_string[i + 1]] - nums[roman_string[i]]
            i += 1
        else:
            res += nums[roman_string[i]]
        i += 1
    return res

print("{} = {}".format("XXIV", roman_to_int("XXIV")))
print("{} = {}".format("MMMCMXCIX", roman_to_int("MMMCMXCIX")))
