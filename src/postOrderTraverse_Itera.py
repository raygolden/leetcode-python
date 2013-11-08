#!/usr/bin/env python

"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def postorder(root):
    q = [root]

    results = []
    while q:
        p = q.pop()

        if not p.left and not p.right:
            results.append(p.value)
        else:
            q.append(p)


        if p.right:
            q.append(p.right)
            p.right = None

        if p.left:
            q.append(p.left)
            p.left = None

    return results





if __name__ == '__main__':
    """   10
          /   \
        8      2
      /  \    /
    3     5  2

    expected: 3 5 8 2 2 10
    """

    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(8, n1, n2)

    n4 = Node(2)
    n5 = Node(2, n4)

    root = Node(10, n3, n5)

    print postorder(root)