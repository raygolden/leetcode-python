#!/usr/bin/env python

" 2 sum in binary search tree "

class Node(object):
    value = None
    left = None
    right = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left;
        self.right = right;
        
    def __str__(self):
        return str(self.value)



class Inorder(object):
    
    def __init__(self, root):
        self.current = root
        self.stack = []
        
    def __iter__(self):
        return self
    
    def next(self):
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
            
        if self.stack:
            self.current = self.stack.pop()
        else:
            raise StopIteration
        
        node = self.current
        self.current = self.current.right
        return node
    
    
class ReverseInorder(object):
    
    def __init__(self, root):
        self.current = root
        self.stack = []
        
        
    def __iter__(self):
        return self
    
    def next(self):
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.right
            
        if self.stack:
            self.current = self.stack.pop()
        else:
            raise StopIteration 
        node = self.current
        self.current = self.current.left
        
        return node



def twoSumBST(root, target):
    inorder = Inorder(root)
    rinorder = ReverseInorder(root)
    results = []
    
    try:
        a = inorder.next()
    except StopIteration:
        return results
    
    try:
        b = rinorder.next()
    except StopIteration:
        return results 
    
    while a.value <= b.value:
        
        if a.value + b.value < target:
            try:
                a = inorder.next()
            except StopIteration:
                break 
        elif a.value + b.value > target:
            try:
                b = rinorder.next()
            except StopIteration:
                break 
            
        else:
            results.append((a.value, b.value))
            
            try:
                a = inorder.next()
            except StopIteration:
                break 
            try:
                b = rinorder.next()
            except StopIteration:
                break 
    
    return results


if __name__ == '__main__':
    """
                  8
                 / \
                3   10
               / \     \
              1  6      14
                /  \    /
                4   7  13    
             
    """
    
    
    node1 = Node(13)
    node2 = Node(14, node1)
    node3 = Node(10, None, node2)
    
    node4 = Node(4)
    node5 = Node(7)
    node6 = Node(6, node4, node5)
    node7 = Node(1)
    node8 = Node(3, node7, node6)
    
    root = Node(8, node8, node3)
    
    print twoSumBST(root, 11)
    