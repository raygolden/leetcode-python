#!/usr/bin/env python
"""
Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

"""
RED = 0
WHITE = 1
BLUE = 2

def swap(A, i, j):
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp
    return A
    

def sortColor(colors):
    cur = 0
    red = 0
    blue = len(colors) - 1
    
    while cur < blue:
        if colors[cur] == RED:
            colors = swap(colors, cur, red)
            cur += 1
            red += 1
            
        elif colors[cur] == BLUE:
            colors = swap(colors, cur, blue)
            blue -= 1
            
        else:
            cur += 1
        
    return colors

print sortColor([1, 0, 2, 2, 1, 2, 1, 1, 0, 2])
    
    