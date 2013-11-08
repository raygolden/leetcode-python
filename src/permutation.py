#!/usr/bin/env python

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
result = []
    
def permutation(s, start=0):
    result.append(''.join(s))
    l = len(s)
    for i in range(start, l):
        for j in range(i + 1, l):
            swap(s, i, j)
            permutation(s, i + 1)
            swap(s, i, j)
            
            
            

if __name__ == '__main__':
    permutation(list('abc'))
    print result