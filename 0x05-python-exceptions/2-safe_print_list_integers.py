#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in my_list:
        try:
            if c < x:
                print("{:d}".format(i), end='')
                c += 1
        except:
            continue
    print()
    return c
