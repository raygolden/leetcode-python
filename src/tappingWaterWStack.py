#!/usr/bin/env python

"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

def tappingWater(bars):
    vol = 0
    cur = 0
    while cur < len(bars) and bars[cur] == 0: cur += 1
    
    stack = []
    while cur < len(bars):

        while stack and bars[stack[-1]] < bars[cur]:
            index = stack.pop()
            if not stack: break
            vol += (cur - index) * (min([bars[stack[-1]], bars[cur]]) - bars[index])
        
        stack.append(cur)
        cur += 1
        
    return vol


print tappingWater([0,1,0,2,1,0,1,3,2,1,2,1])