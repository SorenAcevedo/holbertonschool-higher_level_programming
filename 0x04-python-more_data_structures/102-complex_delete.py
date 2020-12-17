#!/usr/bin/python3
def complex_delete(a_d, value):
    [a_d.pop(k) for k in (a_d.copy()).keys() if a_d.get(k) == value]
    return a_d
