#!/usr/bin/env python
"""
class Solution {
public:
    int divide(int dividend, int divisor) {
        long long a = abs((double)dividend);;
        long long b = abs((double)divisor);

        long long ret = 0;
        while (a >= b) {
            long long c = b;
            for (int i = 0; a >= c; ++i, c <<= 1) {
                a -= c;
                ret += 1 << i;
            }
        }

        return ((dividend^divisor)>>31) ? (-ret) : (ret);
    }
};

"""
import math

def divide(dividend, divisor):
    d1 = int(math.fabs(dividend))
    d2 = int(math.fabs(divisor))

    q = 0

    while d1 >= d2:

        r = d2

        i = 0

        while d1 >= r:
            d1 -= r
            print 'i', i
            q += 1 << i
            print ret

            i +=1
            r = r << 1

    if (dividend ^ divisor) >> 31:
        return -q
    else:
        return q

print divide(6, 3)
