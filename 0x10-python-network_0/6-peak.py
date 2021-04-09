#!/usr/bin/python3
""" Module to find a peak in an array """

def find_peak(list_of_integers):
    """ Function to find a peak """

    if not list_of_integers or len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for i in list_of_integers:
            if i > peak:
                peak = i
    return peak