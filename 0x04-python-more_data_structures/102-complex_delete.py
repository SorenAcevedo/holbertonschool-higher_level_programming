#!/usr/bin/python3
def complex_delete(a_d, value):
    [a_d.pop(k) for k, v in (a_d.copy()).items() if v == value]
    return a_d
