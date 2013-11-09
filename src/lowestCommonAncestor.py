#!/usr/bin/env python

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
        

def lca(root, node1, node2):
    if not root: return None
    
    if (root == node1 or root == node2):
        return root
    
    l = lca(root.left, node1, node2)
    r = lca(root.right, node1, node2)
    
    
    if l and r: return root
    
    if l and not r: return l
    
    if r and not l: return r
    
    return None


if __name__ == '__main__':
    
    """
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
             
    """

    node1 = Node(1)
    node2 = Node(4, None, node1)
    node3 = Node(13)
    node4 = Node(8, node3, node2)
    
    node5 = Node(2)
    node6 = Node(7)
    node7 = Node(11, node6, node5)
    node8 = Node(4, node7)
    
    root = Node(5, node8, node4)
    
    print lca(root, node6, node1).value