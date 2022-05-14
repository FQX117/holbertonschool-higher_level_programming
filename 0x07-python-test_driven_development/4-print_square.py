#!/usr/bin/python3
'''this is a notation'''


def print_square(size):
    '''this is a notation'''

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        None
    else:
        for x in range(size):
            for y in range(size):
                print('#', end='')
            print()
