#!/usr/bin/env python

""" Multiply with bit manipulation """


import math

def multiply(x, y):
    ret = 0
    a = int(math.fabs(x))
    b = int(math.fabs(y))

    while a != 1:
        a = a >> 1
        b = b << 1

        if a & 1:
            ret += b

    if (x >> 31) ^ (y>>31):
        return -ret
    else:
        return ret


if __name__ == '__main__':

    print multiply(4, 5)

    print multiply(-100, 5)

    print multiply(-1000, -5)

    print multiply(-1000, 0)