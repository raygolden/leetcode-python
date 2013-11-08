#!/usr/bin/env python

def isPanlindrome(s, c1, c2):
    i = c1
    j = c2
    while s[i] == s[j] and i > 0 and j < len(s) -1:
        i -= 1
        j += 1
    if s[i] != s[j]: return s[i+1: j]
    return s[i: j + 1]



def longestPalindrome(s):
    l = len(s)
    longest = ''
    ln = 0

    for i in range(l):
        sub = isPanlindrome(s, i, i)
        if len(sub) > ln :
            longest = sub
            ln = len(longest)

        if i < l - 1:
            sub = isPanlindrome(s, i, i+1)

            if len(sub) > ln :
                longest = sub
                ln = len(longest)


    return longest




if __name__ == '__main__':
    print isPanlindrome('aba', 0, 0)

    print isPanlindrome('aba', 1, 1)

    print isPanlindrome('abba', 1, 2)

    print longestPalindrome('abbabbbbbbbbb')