#!/usr/bin/env python

""" Powerset """

def powerset(s):
    s.sort()
    result = []

    result.append([])

    for e in s:
        l = len(result)
        i = 0
        while i < l:
            res = list(result[i])
            res.append(e)

            result.append(res)
            i += 1


    return result


if __name__ == '__main__':
   print powerset([1, 2, 3])