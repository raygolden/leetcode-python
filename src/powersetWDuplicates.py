#!/usr/bin/env python

""" powerset with duplicates """

def powersetWDup(s):
    s.sort()
    results = [[]]
    cur_dup = None

    for elm in s:
        i = 0

        if elm != cur_dup:
            # not a duplicate
            cur_dup = elm
            l = len(results)
            pre = []
            while i < l:
                res = list(results[i])
                res.append(elm)
                results.append(res)
                pre.append(res)
                i += 1
        else:

            l = len(pre)
            while i < l:
                res = list(pre.pop(0))
                res.append(elm)
                results.append(res)
                pre.append(res)
                i += 1

    return results
print powersetWDup([1,2,2,2,3,4])