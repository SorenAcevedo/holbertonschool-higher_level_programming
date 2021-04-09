#!/usr/bin/python3
""" Module to find a peak in an array """


def find_peak(list_of_integers):
    """ Function to find a peak """

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
