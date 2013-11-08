#!/usr/bin/env python
""" longest common prefix"""
def lcp(words):
    words = sorted(words)
    first = words[0]
    last = words[-1]
    pre = ''
    for i in xrange(len(last)):
        if first[i] == last[i]:
            pre += last[i]
        else:
            break

    return pre



print lcp(['flower', 'flow',  'fleet', 'hello'])
