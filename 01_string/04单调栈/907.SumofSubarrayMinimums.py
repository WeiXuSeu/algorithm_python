#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:
1 <= A.length <= 30000
1 <= A[i] <= 30000
"""

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        solution: for A[i]
        (1) find left next minimum j（最近的小值）: (A[j] < A[i]), distance = left(i), 
        (2) find right next minimum k: (A[k] < A[i]), distance = right(i)
        (3) all subnet array contains A[i] : left(i) * right(i)
        f(i) = left(i) * right(i)
        因为可能存在多个值与A[i]相同，如果两侧都是绝对的小于，及两侧都包含相等值，则会重复；
        所以需要一边开，一边关
        若两边都不包含，则会少计算
        [H,K,A,C,K,B,D,K,H] K--min example
        """
        
        if not A:
            return
        # left(i): left next min of A[i] {distance}
        # 维护一个单调递增的stack
        # 在左侧找到一个A[left] <= A[i], 边界, 不包含相等情况,求二者距离
        left_min = [0] * len(A)
        stack = []
        for i in xrange(len(A)):
            while(stack and A[stack[-1]] > A[i]):
                stack.pop()
            left_min[i] = i+1 if not stack else i - stack[-1]
            stack.append(i)
        # right(i): 在右侧找到第一各A[right] < A[i], 边界, 包含相等情况
        right_min = [0] * len(A)
        stack = []
        for i in xrange(len(A)-1, -1, -1):
            while(stack and A[stack[-1]] >= A[i]):
                stack.pop()
            right_min[i] = len(A) - i if not stack else stack[-1] - i
            stack.append(i)
        K = 10**9 + 7
        sum = 0
        for i in xrange(len(A)):
            sum += left_min[i] * right_min[i] * A[i]
        return sum % K
           
 