#!/usr/bin/python3
'''this is a notation'''


def write_file(filename="", text=""):
    '''this is a notation'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
