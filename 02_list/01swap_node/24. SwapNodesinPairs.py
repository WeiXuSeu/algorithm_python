#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        solution1
        """
        
        dummy_header = pNode = ListNode(0)
        dummy_header.next = head
        while pNode.next is not None and pNode.next.next is not None:
            pFirst = pNode.next
            pSecond = pFirst.next
            pNext = pSecond.next
            pNode.next = pSecond
            pSecond.next = pFirst
            pFirst.next = pNext
            pNode = pFirst
        return dummy_header.next
        
        
    def swapPairs1(self, head):
        """
        solution2
        """
        def step_forward(head, steps):
            end = end_next = None
            if not head or steps <= 0:
                return end, end_next
            pCurrent = head
            pNext = head.next
            while steps > 1:
                if not pNext:
                    break
                pNextNext = pNext.next
                pNext.next = pCurrent
                pCurrent = pNext
                pNext = pNextNext
                steps -= 1
            if steps == 1:
                end = pCurrent
                end_next = pNext
            return end, end_next
                
        if not head:
            return 
        dummy_header = pNode = ListNode(0)
        dummy_header.next = head
        pCurrent = dummy_header
        while pCurrent:
            start = pCurrent.next
            end, end_next = step_forward(start, 2)
            # not enough steps, break
            if not end:
                break
            pCurrent.next = end
            start.next = end_next
            pCurrent = start
        return dummy_header.next