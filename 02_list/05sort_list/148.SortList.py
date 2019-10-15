#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # split list to two sub list
        # is slow = fast = head, when list size is 2, dump in infinite loop
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_sub_list = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(second_sub_list)
        return self.merge(left, right)
    
    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        # cannot use dummy, bucause of space limit
        # make sure begin from one specific sub-list, here is left
        # if not, when switch to another sub-list, do know which one
        if left.val > right.val:
            left, right = right, left
        pre = head = left
        left_current = left.next
        while left_current and right:
            if left_current.val <= right.val:
                left_current = left_current.next
            else:
                # merge node meeting condition from right-sub-list to left-sub-list
                right_next = right.next
                right.next = left_current
                pre.next = right
                right = right_next
            # always last node in the merged list (left)
            pre = pre.next
        if right:
            pre.next = right
        return head
        