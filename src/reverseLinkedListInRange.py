#!/usr/bin/env python

"""
Reverse Linked List
Reverse Linked List in Range

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1 -> 2 -> 3 -> 4 -> 5 -> |, m = 2 and n = 4, return 1 -> 4 -> 3 -> 2 -> 5 -> |.

Note: m and n are both 1-based and assume 1 <= m <= n <= list length.
"""

class Node(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node



def reverse_linkedlist_in_range(root, m, n):
    if m == 1:
        first = None
        second = root
        third = second.next_node
    else:
        first = root
        i = 1
        while i < m - 1:
            first = first.next_node
            i += 1

        second = first.next_node
        third = second.next_node

    begin = second

    k = m
    while k < n:
        tmp = third.next_node
        third.next_node = second
        second = third
        third = tmp

        k += 1

    if first:
        first.next_node = second
    else:
        root = second
    begin.next_node = third

    return root


def print_linkedlist(root):
    while root:
        print root.value
        root = root.next_node


if __name__ == '__main__':
    n1 = Node(5)
    n2 = Node(4, n1)
    n3 = Node(3, n2)
    n4 = Node(2, n3)
    n5 = Node(1, n4)
    root = reverse_linkedlist_in_range(n5, 1, 5)
    print_linkedlist(root)
