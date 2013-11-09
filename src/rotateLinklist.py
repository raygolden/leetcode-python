#!/usr/bin/env python

"""
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

class LinkNode(object):
    
    value = None
    next = None
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    
    

def rotateList(linknode, k):
    c = 1
    start = linknode
    fast = slow = start
    
    while c != k:
        fast = fast.next
        c += 1
    fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next

        
    fast.next = start
    new_start = slow.next
    slow.next = None
    
    return new_start



def printList(linknode):
    while linknode:
        print linknode.value, '->',
        linknode = linknode.next
        
if __name__ == '__main__':
    l5 = LinkNode(5)
    l4 = LinkNode(4, l5)
    l3 = LinkNode(3, l4)
    l2 = LinkNode(2, l3)
    l1 = LinkNode(1, l2)

    printList(rotateList(l1, 2))
        