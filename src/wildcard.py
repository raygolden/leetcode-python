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
    if not s:
        if p == '*': return True
        else: return False

    i = 0
    j = 0
    while (i < len(s) and j < len(p)):
        if s[i] == p[j] or p[j] == '?':
            if i == len(s) - 1 and j == len(p) - 1: return True
            i += 1
            j += 1

        elif p[j] == '*':
            if i == len(s) - 1 and j == len(p) - 1: return True
            i += 1

        else:
            return False


    return False


if __name__ == '__main__':
    print isMatch('aa', 'a')
    print isMatch("aa","aa")
    print isMatch("aaa","aa")
    print isMatch("aa", "*")
    print isMatch("aa", "a*")
    print isMatch("ab", "?*")
    print isMatch("aab", "c*a*b")
    print isMatch("aab", "*a*b")
    print isMatch("aabccc", "*ccc")