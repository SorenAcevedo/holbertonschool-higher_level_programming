#!/usr/bin/python3
""" Module to find a peak in an array """


def find_peak(list_of_integers):
    """ Function to find a peak """

    leng = len(list_of_integers)
    if not list_of_integers or leng == 0:
        return None

    else:
        list_of_integers.sort()
        return list_of_integers[-1]
