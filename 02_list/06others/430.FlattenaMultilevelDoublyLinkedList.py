#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given a doubly linked list which in addition to the next and previous pointers, 
it could have a child pointer, which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, and so on, 
to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. 
You are given the head of the first level of the list.

Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        self.flatten_core(head)
        return head
        
    def flatten_core(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return
        if head.child is None and head.next is None:
            return
        self.flatten(head.child)
        if head.child:
            head_next = head.next
            head_child = head.child
            child_tail = head_child
            while child_tail.next:
                child_tail = child_tail.next
            if head_next:
                child_tail.next = head_next
                head_next.prev = child_tail
            head.next = head.child
            head.child.prev =head
            head.child = None
        self.flatten(head.next)

