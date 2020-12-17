#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        rs = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(len(roman_string)):
            if i < len(roman_string) - 1:
                if rs.get(roman_string[i]) < rs.get(roman_string[i + 1]):
                    num += rs.get(roman_string[i + 1]) - 1
                    if i == len(roman_string) - 2:
                        break
                else:
                    num += rs.get(roman_string[i])
            else:
                num += rs.get(roman_string[i])
        return num
    return 0
