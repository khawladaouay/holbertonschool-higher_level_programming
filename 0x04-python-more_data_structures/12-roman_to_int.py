#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    for i in range(len(roman_string)):
        if i + 1 != len(roman_string) and rom[roman_string[i]] <\
                rom[roman_string[i + 1]]:
            s -= rom[roman_string[i]]
        else:
            s += rom[roman_string[i]]
    return s
