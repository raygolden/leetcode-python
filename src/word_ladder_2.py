#!/usr/bin/env python
"""
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

def diff(s1, s2):
    num = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            num += 1
            
    return num


def word_ladder(start, end, d):
 
    q = [(start, [start])]
    min = 100000
    
    while q:
        p = q.pop()
        
        if diff(p[0], end) == 1:
            p[1].append(end)
            if len(p[1]) < min:
                min = len(p[1])
        
        else:
            for w in d:
                if diff(w, p[0]) == 1 and w not in p[1]:
                    q.append((w, p[1] + [w]))
            
    return min
        
print word_ladder("hit", "cog", ["hot","dot","dog","lot","log"])