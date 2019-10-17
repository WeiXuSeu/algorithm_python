#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def postorderTraversalCore(root: TreeNode) -> List[int]:
            if not root:
                return
            postorderTraversalCore(root.left)
            postorderTraversalCore(root.right)
            result.append(root.val)
        
        postorderTraversalCore(root)
        return result
        
    """
    solution2: iterative
    后续遍历: 左右头，
    后续的逆序： 头右左
    前序遍历：头左右， 故后续的逆序可以参照前序来写
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        result = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            while cur:
                result.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                cur = cur.right
        return reversed(result)
                
                
                
                
