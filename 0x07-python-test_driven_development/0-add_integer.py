#!/usr/bin/python3
'''this is a notation'''


def add_integer(a, b=98):
    '''this is a notation'''
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) != int:
        if type(b) == float:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
