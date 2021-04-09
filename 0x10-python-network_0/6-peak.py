#!/usr/bin/python3
""" Module to find a peak in an array """


def find_peak(list_of_integers):
    """ Function to find a peak """

    leng = len(list_of_integers)
    if not list_of_integers or leng == 0:
        return None

    if leng > 2:
        peak = list_of_integers[leng // 2]
        right = list_of_integers[(leng // 2) + 1]
        left = list_of_integers[(leng // 2) - 1]
        if left < peak > right:
            return peak
        elif left < peak:
            return find_peak(list_of_integers[(leng // 2) + 1:])
        else:
            return find_peak(list_of_integers[:leng // 2])
    else:
        return max(list_of_integers)
