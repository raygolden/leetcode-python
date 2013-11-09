#!/usr/bin/env python

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

def firstPositiveInteger(A):
    l = len(A)
    i = 0
    
    while i < l:
        if A[i] > 0:
            new_pos = A[i] % l - 1
            tmp = A[new_pos]
            A[new_pos] = A[i]
            A[i] = tmp
        else:
            A[i] = None
            
        i += 1
            
    for i in xrange(l):
        if A[i] is None:
            break
        
    return A[i-1] + 1
        
    
            
            
    
if __name__ == '__main__':
    print firstPositiveInteger([1,2,0])
    print firstPositiveInteger([3,4,-1,1])
    print firstPositiveInteger([7, 8, 5])