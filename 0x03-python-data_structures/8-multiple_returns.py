#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = (len(sentence), sentence[0])
    else:
        a = (0, None)
    return a
