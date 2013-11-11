#!/usr/bin/env python

"""
Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

Your algorithm's runtime complexity must be in the order of O(log n).

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

def binarySearchWithDuplicate(arr, target):
    left = 0
    right = len(arr) - 1
    start = -1
    end = -1
    
    while left < right:
        
        mid = left + (right - left) / 2
        if target == arr[mid]:
            if mid == 0 or arr[mid-1] != arr[mid]:
                # beginning
                start = mid
                right = len(arr) - 1
                left = mid + 1
                
            if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                # ending
                end = mid
                right = mid - 1
                left = 0
                
            if start > 0 and end > 0:
                return [start, end]
                
            if start == -1:
                right = mid - 1
            else:
                left = mid + 1
                
        
        elif target < arr[mid]:
            right = mid - 1
            
        elif target > arr[mid]:
            left = mid + 1
            
    return [start, end]
    

if __name__ == '__main__':
    print binarySearchWithDuplicate([1, 2, 3, 3, 3, 3, 4, 5, 6], 3)