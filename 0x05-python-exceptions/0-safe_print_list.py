#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        flag = 1
        for i, j in enumerate(my_list):
            if i >= x:
                flag = 0
                break
            print(j, end='')
        print()
        return i + flag
    except:
        print()
        return i + flag
