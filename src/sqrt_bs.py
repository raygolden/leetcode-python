#!/usr/bin/env python

def sqrt(n):
    if n < 2 : return n

    left = 0
    right = n

    while left < right - 1:
        mid = left + (right - left) / 2

        div = n / mid

        if div == mid: return div

        if div > mid: left = mid
        else: right = mid

    return div

if __name__ == '__main__':
    print sqrt(4)
    print sqrt(8)
    print sqrt(255)