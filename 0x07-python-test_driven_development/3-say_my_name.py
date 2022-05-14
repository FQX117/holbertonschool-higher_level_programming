#!/usr/bin/python3
'''this is a notation'''


def say_my_name(first_name, last_name=""):
    '''this is a notation'''

    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    if last_name == "":
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
