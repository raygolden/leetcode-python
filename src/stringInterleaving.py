#!/usr/bin/env python

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca", 

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

def isInterleaving(s1, s2, s3):
    k = 0
    q = [(k, [(0, 0)])] # examing s3 k position, (0, 0) is examing s1 and s3 position
    l3 = len(s3)

    while q:
        
        k, out = q.pop()
        i, j = out[-1]
        if k == l3 and i + j == l3: return True
        if i < len(s1)  and s3[k] == s1[i] and k  < l3:
            q.append((k + 1, out + [(i + 1, j)]))
        
        if j < len(s2) and s3[k] == s2[j] and k  < l3 :
            q.append((k + 1, out + [(i, j + 1)]))
        

    
    return False

if __name__ == '__main__': 
    print isInterleaving("aabcc", "dbbca", "aadbbcbcac")
    print isInterleaving("aabcc", "dbbca", "aadbbbaccc")