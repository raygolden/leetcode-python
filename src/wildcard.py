#!/usr/bin/env python

"""
Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "*") ? true
isMatch("aa", "a*") ? true
isMatch("ab", "?*") ? true
isMatch("aab", "c*a*b") ? false
"""


def isMatch(s, p):
    if s and p:
        if s[0] == p[0] or p[0] == '?':
            return isMatch(s[1:], p[1:])

        elif p[0] == '*':
            star = 0
            index = 0
            while star < len(p) and p[star] == '*': star += 1
            if star == len(p): return True
            while index < len(s):
                if isMatch(s[index:], p[star:]):
                    return True
                index += 1

    else:
        if p and not s:
            if p == '*':
                return True
            else:
                return False
        elif not p and not s:
            return True



    return False


if __name__ == '__main__':
    print isMatch('aa', 'a') # False
    print isMatch("aa","aa") # True
    print isMatch("aaa","aa") # False
    print isMatch("aa", "*") # True
    print isMatch("aa", "a*") #True
    print isMatch("ab", "?*") #True
    print isMatch("aab", "c*a*b") #False
    print isMatch("aab", "*a*b") # True
    print isMatch("aabccc", "*ccc") #True