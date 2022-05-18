#!/usr/bin/python3
'''this is a notation'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''this is a notation'''
    def __init__(self, size):
        '''this is a notation'''
        self.__size = size
        self.integer_validator('width', size)
        super().__init__(size, size)
