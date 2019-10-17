#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        stack1 = []
        stack2 = []
        """
        python中需要注意此种写法，否则实际上指向同一地址
        stack1 = stack2 = []
        """
        if root is None:
            return result
        curr = root
        stack1.append(root)
        i = 0
        while stack1:
            list_item = [x.val for x in stack1]
            result.append(list_item)
            if i % 2 == 0:
                for index in range(len(stack1)-1, -1, -1):
                    if stack1[index].right:
                        stack2.append(stack1[index].right)
                    if stack1[index].left:
                        stack2.append(stack1[index].left)
            else:
                for index in range(len(stack1)-1, -1, -1):
                    if stack1[index].left:
                        stack2.append(stack1[index].left)
                    if stack1[index].right:
                        stack2.append(stack1[index].right)
            stack1 = stack2
            stack2 = []
            i += 1
        return result

