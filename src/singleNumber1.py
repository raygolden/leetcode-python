#!/usr/bin/env python
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

def singleNumber(arr):
    s = arr[0]
    for elm in arr[1:]:
        s = s ^ elm

    return s

if __name__ == '__main__':
    print singleNumber([1, 2, 2, 1, 3])

