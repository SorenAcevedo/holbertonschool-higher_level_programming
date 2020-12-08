#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    n = num * -1
else:
    n = num
if n % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, n % 10))
elif n % 10 == 0:
    print("Last digit of {} is 0 and is 0".format(num))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        num, n % 10))
