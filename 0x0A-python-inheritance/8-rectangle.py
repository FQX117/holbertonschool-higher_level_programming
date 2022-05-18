#!/usr/bin/python3
'''this is a notation'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''this is a notation'''
    def __init__(self, width, height):
        '''this is a notation'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
