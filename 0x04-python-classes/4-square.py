#!/usr/bin/python3
'''a class for square'''
class Square:
    '''this is class'''
    def __init__(self, size=0):
        self.size = size
    def area(self):
        return(self.__size * self.__size)
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
