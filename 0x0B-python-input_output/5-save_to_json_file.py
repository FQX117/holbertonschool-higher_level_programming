#!/usr/bin/python3
'''this is a notation'''
import json


def save_to_json_file(my_obj, filename):
    '''this is a notation'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
