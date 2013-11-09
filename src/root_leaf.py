#!/usr/bin/env python

"""
Sum Root to Leaf Numbers Total Accepted: 2625 Total Submissions: 9605 My Submissions
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

class Node:
    left = None
    right = None
    value = None
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def root_leaf(root):
    result = []
    q = []
    
    q.append((root, root.value))
    
    while q:
        n = q.pop()
        
        if n[0].left:
            q.append((n[0].left, n[1] * 10 + n[0].left.value))
            
        if n[0].right:
            q.append((n[0].right, n[1] * 10 + n[0].right.value))
            
        if not n[0].left and not n[0].right: # leave node
            result.append(n[1])
            

    return sum(result)
    
        
    
root = Node(1, Node(2), Node(3))
    
print root_leaf(root)
