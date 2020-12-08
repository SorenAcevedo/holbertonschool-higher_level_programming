#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = number * -1
    else:
        n = number
    print(n % 10, end = "")
    return n % 10

