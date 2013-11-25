#!/usr/bin/env python

"""Sort a linked list using insertion sort."""

class Node(object):
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
       

def sortLinkedListInsertionSort(node):
    prev = node
    ptr1 = node.next
    
    
    while ptr1:
        ptr2 = node
        prev2 = None
        while ptr2.value < ptr1.value and ptr1 != ptr2:
            prev2 = ptr2
            ptr2 = ptr2.next
            
        if ptr2 == ptr1:
            prev = prev.next
            ptr1 = ptr1.next
            continue
        
        if ptr2 == node:
            # at the beginning
            prev.next = ptr1.next
            ptr1.next = node
            node = ptr1
            
        else:
            prev.next = ptr1.next
            prev2.next = ptr1
            ptr1.next = ptr2
            
        ptr1 = prev.next
        

    return node
    
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
    
    root = sortLinkedListInsertionSort(n10)
    next = root
    while next:
        print next.value
        next = next.next
    