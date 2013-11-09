#!/usr/bin/env python

def addOne(num):
    if not num:
            return [1]
    
    if num[-1] != 9:
            return num[:-1] + [ num[-1] + 1]
    
    return addOne(num[:-1]) + [0]
                
                
                

print addOne([])

print addOne([9])

print addOne([1, 2, 3])

print addOne([9, 9, 9])

print addOne([1, 19, 9, 9])