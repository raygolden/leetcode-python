#!/usr/bin/env python

"""You are given a binary tree in which each node contains a value. Design an algorithm to print all paths which sum to a given value.
The path does not need to start or end at the root or a leaf.
"""

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        


def subFindSum(node, sum, path, level):
    if not node: return
    
    path[level] = node.value
    
    t = 0
    for i in range(level, -1, -1):
        t += path[i]
        if t == sum:
            print path[i: level + 1]
            
    subFindSum(node.left, sum, path, level + 1)
    subFindSum(node.right, sum, path, level + 1)
    
    path[level] = -99999999



def getHeight(node):
    if not node: return 0
    return 1 + max([getHeight(node.left), getHeight(node.right)])
    

def findSum(node, sum):
    depth = getHeight(node)
    path = [0] * depth
    
    subFindSum(node, sum, path, 0)
    
    
if __name__ == '__main__':
    n1 = Node(2)
    n2 = Node(3)
    n3 = Node(1, n1, n2)
    n4 = Node(2)
    root = Node(-1, n3, n4)
    
    findSum(root, 3)