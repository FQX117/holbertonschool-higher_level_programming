#!/usr/bin/python3
n = 00
while n < 100:
    if n <= 98:
        print("{:02}, ".format(n), end="")
    else:
        print("{:02}".format(n))
