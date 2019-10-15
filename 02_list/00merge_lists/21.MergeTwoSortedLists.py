#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge two sorted linked lists and return it as a new list. The new list should be made 
by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists0(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        """
        solutin1: recursion
        """
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            header = ListNode(l1.val)
            header.next = self.mergeTwoLists(l1.next, l2)
        else:
            header = ListNode(l2.val)
            header.next = self.mergeTwoLists(l1, l2.next)
        return header
     
    
    def mergeTwoLists1(self, l1, l2):
        """
        solution2: iteration
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next
        
        
