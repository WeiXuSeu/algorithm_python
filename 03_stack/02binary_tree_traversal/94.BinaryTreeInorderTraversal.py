#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    solution1: recursive
    """
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        result = []
        def inorderTraversalCore(root: TreeNode) -> List[int]:
            if not root:
                return
            inorderTraversalCore(root.left)
            result.append(root.val)
            inorderTraversalCore(root.right)
        inorderTraversalCore(root)
        return result
    
    """
    solution2: iterative
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        stack = []
        cur = root
        while cur or stack:
            # append all left child (contain it self)
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            result.append(node.val)
            if node.right:
                cur = node.right
        return result
            
            