#!/usr/bin/env python

"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

d = set(["cat", "cats", "and", "sand", "dog"])

def isInDict(word):
    return word in d


def word_break_2(s):
    q = []
    output = []
    visited = set([])
    left = 0
    right = len(s) - 1
    q.append((left, right))
    
    while q:
        left, right = q.pop()
        print s[:left + 1], s[left + 1: right], s[right:]
        visited.add((left, right))
        if isInDict(s[:left + 1]) and isInDict(s[right:]) and isInDict(s[left + 1: right]):
            
            output.append(" ".join([s[:left + 1], s[left + 1: right], s[right:]]))
            
        if left < right - 2:
            if (left, right - 1) not in visited:
                q.append((left, right - 1))
            if (left + 1, right) not in visited:
                q.append((left + 1, right))
            if (left + 1, right -1 ) not in visited:
                q.append((left + 1, right - 1))
    return output           
                
print word_break_2("catsanddog")