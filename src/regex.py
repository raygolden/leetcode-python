#!/usr/bin/env python

"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

def isMatch(p, s):
    if p and s:
        if p[0] == s[0]:
            return isMatch(p[1:], s[1:])
        elif p[0] == '.':
            if len(s) > 2 and s[1] == '*':
                return isMatch(p[1:], s[2:])
    else:
        if not p and not s:
            return True


    return False

