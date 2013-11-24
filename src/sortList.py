#!/usr/bin/env python

"""
Sort List
Sort a linked list in O(n log n) time using constant space complexity.
"""

class Node(object):
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
       

def mergeList(left, right):
    # merge left and right
    if left and not right: return left
    if right and not left: return right
    
    if left.value < right.value:
        tmp = left
        left = right
        right = tmp
        
    head = right
    
    while left and right:
        if right.next:
            if left.value < right.next.value:
                # insert
                new_right = right.next
                left_end = left
                while left_end.next and left_end.next.value < right.next.value:
                    left_end = left_end.next
                new_left = left_end.next
                
                right.next = left
                left_end.next = new_right
                left = new_left
                right = new_right
            else:
                right = right.next
    
        else:
            right.next = left
            break
            
    return head

def sortList(node):
    c = 1
    fast = node
    slow = node
    
    while fast and fast.next:
        if fast.next.next:
            fast = fast.next.next
            c += 2
            slow = slow.next
        else:
            fast = fast.next
            c += 1
            
    if c == 2:
        if slow.value > fast.value:
            fast.next = slow
            slow.next = None
            #print 'fast', fast.value
            return fast
        else:
            return slow
    elif c == 1:
        return node
    else:
        right = sortList(slow.next)
        slow.next = None
        left = sortList(node)
        return mergeList(left, right)
        
                    
                    
    
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
    root = sortList(n10)
    next = root
    while next:
        print next.value
        next = next.next
    