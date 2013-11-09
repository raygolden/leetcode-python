#!/usr/bin/env python

"""
Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example, S = "ADOBECODEBANC",  T = "ABC",
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".
If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""


def minWindowSubstring(S, T):
        
    minWindow = ''
    d = {} # used to trace duplicates
    
    for a in T:
        d[a] = 0
        
    l = len(S)
    
    left = 0
    right = 0
    
    found = [] # positions of found element
    tobefound = set(list(T))
    while right < l:
          
        if S[right] in d:
            d[S[right]] += 1
            
            found.append(right)
            
            if S[right] in tobefound:
                tobefound.remove(S[right])
                
           
            while len(tobefound) == 0: # found everything
                if not minWindow or len(minWindow) > found[-1] - found[0] + 1:
                    minWindow = S[found[0]: found[-1] + 1]
                    
                left = found.pop(0)
                d[S[left]] -= 1
                if d[S[left]] == 0:
                    tobefound.add(S[left])
                
        right += 1
    
    return minWindow


print minWindowSubstring("ADOBECODEBANC", 'ABC')
print minWindowSubstring("ADOBECODEBANC", 'ABCK')