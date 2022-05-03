#!/usr/bin/python3
n = 00
while n < 100:
    if n <= 98:
        print("{:02}, ".format(n), end="")
        n = n+1
    else:
        print("{:02}".format(n))
