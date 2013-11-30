#!/usr/bin/env python

class Node(object):
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
        
        
def findMiddleLinkList(start):
    fast = start
    slow = start
    
    while fast and fast.next:
        if fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        else:
            break
    return slow
            
if __name__ == '__main__':
    n1 = Node(12)
    n2 = Node(11, n1)
    n3 = Node(5, n2)
    n4 = Node(3, n3)
    n5 = Node(2, n4)
    
    n6 = Node(10, n5)
    n7 = Node(7, n6)
    n8 = Node(6, n7)
    n9 = Node(4, n8)
    n10 = Node(1, n9)
    
    #root = mergeList(n5, n10)
    root = findMiddleLinkList(n3)
    print root.value