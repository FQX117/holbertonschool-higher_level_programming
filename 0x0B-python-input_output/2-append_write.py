#!/usr/bin/python3
'''this is a notation'''


def append_write(filename="", text=""):
    '''this is a notation'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
