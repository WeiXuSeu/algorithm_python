#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None:
            return lists
        from heapq import heappush, heappop, heapreplace, heapify
        dummy_header = pNode = ListNode(0)
        heap = [(x.val, x) for x in lists if x is not None]
        heapify(heap)
        while heap:
            min_val, min_list = heappop(heap)
            pNode.next = min_list
            pNode = pNode.next
            if min_list.next is not None:
                heappush(heap, (min_list.next.val, min_list.next))
        return dummy_header.next