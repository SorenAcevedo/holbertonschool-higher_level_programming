#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """ Indent text """

    separadores = ":?."
    j = 0

    if type(text) != str:
        raise TypeError('text must be a string')

    while text[j] == ' ':
        j += 1

    print(text[j], end="")
    i = j + 1

    while i < len(text):
        if text[i - 1] in separadores:
            print("\n")
            if text[i] != ' ':
                print("{}".format(text[i]), end="")
                i += 1
            else:
                while text[i] == ' ':
                    i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1

    if text[i - 1] in separadores and i > 0:
        print("\n")
