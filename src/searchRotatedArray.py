#!/usr/bin/env python

"""
Search in Rotated Sorted Array - No Duplicates

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Given a target value to search, return its index if found in the array, otherwise return -1.

You may assume no duplicate exists in the array.
"""

def searchRotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) / 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            if target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

        elif target < arr[mid]:
            if target >= arr[left]:
                right = mid - 1
            else:
                left = mid + 1


    return -1



print searchRotated([4, 5, 6, 7, 0, 1, 2], 4)
print searchRotated([4, 5, 6, 7, 0, 1, 2], 5)
print searchRotated([4, 5, 6, 7, 0, 1, 2], 0)
print searchRotated([4, 5, 6, 7, 0, 1, 2], 2)
print searchRotated([7, 0, 1, 2, 4, 5, 6], 7)