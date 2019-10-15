#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        current = head
        val_list = []
        while current:
            val_list.append(current.val)
            current = current.next
        right = len(val_list) - 1
        current = head
        for index in range(0, (len(val_list) + 1)/2, 1):
            if current: 
                current.val = val_list[index]
            if current.next:
                current.next.val = val_list[right - index]
                current = current.next.next
