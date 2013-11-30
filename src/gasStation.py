#!/usr/bin/env python

def gasStation(gas=[], cost=[]):
    
    n = len(gas)
    start = 0
    while start < n:
        
        tank = 0
        found = True
        
        for j in xrange(start, n + start):
            cur = j % n
            tank -= cost[cur]
            tank += gas[cur]
            
            if tank < 0:
                start = j + 1;
                found = False
                break
            
            
        if found: break
            
        if start >= n: return -1
    return start


if __name__ == '__main__':
    print gasStation([1, 2], [2, 1])
    print gasStation([2,3,1], [3,1,2])
    print gasStation([4], [5])
    print gasStation([3, 4], [4, 4])