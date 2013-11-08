#!/usr/bin/env python

# find median of unsorted array

def partition(a):
    j = 0
    i = j - 1
    p = a[-1]
    for j in xrange(0, len(a) - 1):
        if a[j] < p:
            i += 1
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp

    a[-1] = a[i + 1]
    a[i+1] = p


    return i + 1, a


def findKth(a, k):
    l = len(a)
    #if l == 0: return
    #if l == 1: return a[0]
    if k > l: return 
    q, a = partition(a)


    if q + 1 == k:
        return a[q]
    elif q + 1 > k:
        return findKth(a[:q], k)
    else:
        return findKth(a[q + 1:], k - q - 1)
print findKth([10, 3, 2, 1, 5, 6, 8], 5)

def findMedian(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    l  = l1 + l2
    if (l % 2 != 0):
        return findKth(a1 + a2, l / 2 + 1)
    else:
        return (findKth(a1 + a2, l / 2) + findKth(a1 + a2, l / 2 + 1)) / 2

print findMedian([1, 3, 5], [2, 7])