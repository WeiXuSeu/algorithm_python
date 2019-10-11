#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1171. Remove Zero Sum Consecutive Nodes from Linked List

Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that 
sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        solution:
        (1) 将node list转换为value array
        (2) 因为需要去除sub_seq，所以最好另起一个target list，方便增加删除
                states维护target list的状态，
                在删除sub_seq前，需要去除其包含的states状态
        """
        
        if not head:
            return
        ori_list = []
        cur = head
        # node list to value list
        while cur:
            ori_list.append(cur.val)
            cur = cur.next
        target_list = []
        states = {}
        # init states[0] = -1, align to other conditions
        states[0] = -1
        sum_ = 0
        for i in xrange(len(ori_list)):
            # 构造target_list, 遇到sub_seq:0时，弹出
            target_list.append(ori_list[i])
            sum_ += ori_list[i]
            if sum_ in states:
                """
                回复states状态后，删除sub_seq:0
                """
                index = states[sum_]
                sum_cur = sum_
                # 删除由该子串构成的states状态
                # 删除[index+1, target-1]的状态，需要减去[index+2,target]
                for i in range(len(target_list)-1, index+1, -1):
                    sum_cur -= target_list[i]
                    states.pop(sum_cur)
                target_list = target_list[:index+1]
            else:
                # states中记录target list中对应的sum:list
                states[sum_] = len(target_list) - 1
        if not target_list:
            return
        target_listNode = [ListNode(x) for x in target_list]
        for i in xrange(len(target_list) - 1):
            target_listNode[i].next = target_listNode[i+1]
        return target_listNode[0]
