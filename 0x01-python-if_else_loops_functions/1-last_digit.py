#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number * -1
else:
    n = number
if n % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, n % 10))
elif n % 10 == 0:
    print("Last digit of {} is 0 and is 0".format(number))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, n % 10))