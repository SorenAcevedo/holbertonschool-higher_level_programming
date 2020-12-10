#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l = len(argv) - 1

    if l == 0:
        print("0 arguments.")
    elif l == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(l))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
