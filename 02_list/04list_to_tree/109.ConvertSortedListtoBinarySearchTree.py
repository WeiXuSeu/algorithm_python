#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following 
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return head
        node = head
        value_list = []
        while node is not None:
            value_list.append(node.val)
            node = node.next
        left_index = 0
        right_index = len(value_list) - 1
        root_node = self.sortedListToBSTCore(value_list, left_index, right_index)
        return root_node
    
    def sortedListToBSTCore(self, value_list, left, right):
        """
        try to assign equal nodes (not bigger than 1) to each left & right child;
        from big sub tree to child sub tree, keep the balance
        """
        if value_list is None or left > right:
            return
        if left == right:
            tree_node = TreeNode(value_list[left])
            return tree_node
        root_index = (right-left+1)/2 + left
        root_node = TreeNode(value_list[root_index])
        root_node.left = self.sortedListToBSTCore(value_list, left, root_index-1)
        root_node.right = self.sortedListToBSTCore(value_list, root_index+1, right)
        return root_node
