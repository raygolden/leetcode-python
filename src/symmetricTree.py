#!/usr/bin/env python

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3

"""

class Node(object):
    
    value = None
    left = None
    right = None
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def symmetricTree(root):
    stack = []
    
    q = [root]
    while q:
        v = q.pop(0)
        if v:
            q.append(v.left)
            q.append(v.right)
            
        if stack:
            if v is not None:
                if stack[-1] == v.value:
                    stack.pop()
                    
                else:
                    stack.append(v.value)
            else:
                if stack[-1] is None:
                    stack.pop()
                else:
                    stack.append(None)
                
        else:
            if v is not None:
                stack.append(v.value)
            else:
                stack.append(None)
            
            
    return len(stack) == 1
    

if __name__ == '__main__':
    n3 = Node(3)
    n4 = Node(4)
    n31 = Node(3)
    n41 = Node(4)
    n2 = Node(2, n3, n4)
    n21 = Node(2, n41, n31)
    
    root = Node(1, n2, n21)
    
    print symmetricTree(root)
    
    n22 = Node(2, None, n3)
    n23 = Node(2, None, n31)
    
    root1 = Node(1, n22, n23)
    print symmetricTree(root1)