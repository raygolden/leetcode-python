#!/usr/bin/env python

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


class node(object):
    value = None
    left = None
    right = None

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left;
        self.right = right;

    def __unicode__(self):
        return str(self.value)



def reconstruct_tree(preorder, inorder):

    if not preorder: return None
    root = node(preorder[0])
    if not inorder: return None
    i = inorder.index(root.value)
    left = inorder[:i]
    right = inorder[i+1:]

    root.left = reconstruct_tree(preorder[1:i + 1], left)
    root.right = reconstruct_tree(preorder[i + 1:], right)

    return root




if __name__ == '__main__':
    
    tree = reconstruct_tree([7, 10, 4, 3, 1, 2, 8, 11], [4, 10, 3, 1, 7, 11, 8, 2])
    print_tree(tree)