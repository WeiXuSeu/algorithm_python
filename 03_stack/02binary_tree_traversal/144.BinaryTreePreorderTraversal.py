#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    method1: recursion
    """
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        result = []
        def preorderTraversalCore(root: TreeNode) -> List[int]:
            if not root:
                return
            result.append(root.val)
            preorderTraversalCore(root.left)
            preorderTraversalCore(root.right)
        preorderTraversalCore(root)
        return result
    
    """
    method2: iterative
    while iterate:
        (1) get the top stack node
        (2) get its value
        (3) keep its right node
        (4) iterate to its left node to get its value
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            while cur:
                result.append(cur.val)
                if cur.right:
                    stack.append(cur.right) 
                cur = cur.left
        return result

