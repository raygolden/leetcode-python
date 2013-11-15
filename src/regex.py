#!/usr/bin/env python

"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "a*") true
isMatch("aa", ".*")  true
isMatch("ab", ".*")  true
isMatch("aab", "c*a*b")  true
"""

def isMatch(s, p):
    if p and s:
        if p[0] == s[0] or p[0] == ".":
            if len(p) > 1 and p[1] == '*':
                return isMatch(s[1:], p)
            return isMatch(s[1:], p[1:])
        else:
            if len(p) > 1 and p[1] == '*':
                return isMatch(s, p[2:])                
                
    elif not p and not s:
        return True
        
    elif p and not s:
        if len(p) == 2 and p[1] == '*': return True


    return False



print isMatch("aa","a")
print isMatch("aa","aa")
print isMatch("aaa","aa")
print isMatch("aa", "a*")
print isMatch("aa", ".*")
print isMatch("ab", ".*")
print isMatch("aab", "c*a*b")
print isMatch('abcde', ".b*de")