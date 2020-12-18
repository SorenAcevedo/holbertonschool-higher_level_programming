#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ac = rs.get(roman_string[0])
        num = 0
        for i in range(1, len(roman_string)):
            if ac < rs.get(roman_string[i]):
                num -= ac
            else:
                num += ac
            ac = rs.get(roman_string[i])
        num += ac
        return num
    return 0
