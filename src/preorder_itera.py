#!/usr/bin/env python

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
        

def preorder(root):
    s = []
    s.append(root)
    
    while s:
        n = s.pop()
        print n.value
        
        if n.right:
            s.append(n.right)
        
        if n.left:
            s.append(n.left)



if __name__ == '__main__':
    """  10
          /   \
        8      2
      /  \    /
    3     5  2
    
    expected: 10 8 3 5 2 2
    """
    
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(8, n1, n2)
    
    n4 = Node(2)
    n5 = Node(2, n4)
    
    root = Node(10, n3, n5)
    
    
    preorder(root)
    