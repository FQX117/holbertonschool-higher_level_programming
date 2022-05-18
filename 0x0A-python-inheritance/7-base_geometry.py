#!/usr/bin/python3
'''this is a notation'''


class BaseGeometry:
    '''this is a notation'''
    def area(self):
        '''this is a notation'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''this is a notation'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
