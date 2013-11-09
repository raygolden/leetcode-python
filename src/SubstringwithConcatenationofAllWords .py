#!/usr/bin/env python

"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""


def findSubstring(S, L):
    output = []
    words = {}
    for w in L:
        words[w] = 1
        
    word_len = len(L[0])
    s_len = len(S)
    total_word = len(L)
    
    
    for i in xrange(word_len):
        wordscollected = set(L)
        begin = j = i
        
        cut = (s_len - i)/ word_len
        
        while begin < cut * word_len - total_word * word_len and j < cut * word_len - word_len:
            
            sub = S[j:j + word_len]
            
            if sub in words:
                # is the word we are looking for
                if sub in wordscollected:
                    # no duplicate
                    wordscollected.remove(sub)
                    j += word_len
                    
                    if len(wordscollected) == 0:
                        output.append(begin)
                        wordscollected.add(S[begin:begin + word_len])
                        begin += word_len
                        
                
                else:
                    # duplicate
                    wordscollected.add(S[begin: begin + word_len])
                    begin += word_len
                    
            else:
                # not the word we are looking for, reset and move on
                j += word_len
                begin = j
                wordscollected = set(L)
                
        
                
                
    return output


print findSubstring("barfoothefoobarman", ["foo", "bar"])
print findSubstring("barabcfoothefoobarman", ["foo", "bar"])
print findSubstring("barabcfoofootheabcfoobarman", ["foo", "bar", "abc"])
        