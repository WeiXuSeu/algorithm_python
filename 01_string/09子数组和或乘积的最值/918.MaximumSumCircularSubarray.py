#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a circular array C of integers represented by A, find the maximum possible 
sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j 
with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
"""

class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        solution1:
        (1) no circle, find max subarray
        (2) have circle, find min subarry, [sum-min_sub]
        (3) find the max of the both
        """
        if not A:
            return A
        max_ = A[0]
        has_plus = False
        has_minus = False
        sum_ = 0
        for x in A:
            sum_ += x
            if x < 0:
                has_minus = True
            elif x > 0:
                has_plus = True
            max_ = max(max_, x)
        if not has_plus:
            return max_
        if not has_minus:
            return sum_
                
        # no circle, find max subarray
        result = A[0]
        sum_sub = A[0]
        for x in A[1:]:
            if sum_sub > 0:
                sum_sub += x
            else:
                sum_sub = x
            result = max(result, sum_sub)
        # contain circle, find minimum subarray
        sum_sub = A[0]
        result_min = A[0]
        for x in A[1:]:
            if sum_sub < 0:
                sum_sub += x
            else:
                sum_sub = x
            result_min = min(result_min, sum_sub)
        return max(result, sum_ - result_min)
            
        