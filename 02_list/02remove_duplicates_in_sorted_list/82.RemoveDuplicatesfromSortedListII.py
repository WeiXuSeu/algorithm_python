#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        """
        solution: keep prev
        (1) from first dummy node, find one value after duplicate node
        (2) link to this one after duplicate node
        (3) loop (1) for this node
        """
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        pCurrent = dummy.next
        while pCurrent:
            pNext = pCurrent.next
            is_duplicate = False
            # find one node after duplicate node
            while pNext and pCurrent.val == pNext.val:
                pNext = pNext.next
                is_duplicate = True
            # relink depend on whether duplicate
            """
            if duplicate, jump this node
            else link to this node
            need to keep, pPrev, pCur, pNext
            """
            if is_duplicate:
                # prev no change
                prev.next = pNext
            else:
                # prev update
                prev.next = pCurrent
                prev = pCurrent
            pCurrent = pNext   
        return dummy.next