#!/usr/bin/python3
'''this is a notation'''
import json


def load_from_json_file(filename):
    '''this is a notation'''
    with open(filename) as f:
        return json.load(f)
