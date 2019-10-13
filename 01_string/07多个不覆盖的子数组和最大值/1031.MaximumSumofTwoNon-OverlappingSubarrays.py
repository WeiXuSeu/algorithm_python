#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1031. Maximum Sum of Two Non-Overlapping Subarrays

Given an array A of non-negative integers, return the maximum sum of elements in 
two non-overlapping (contiguous) subarrays, which have lengths L and M.  
(For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
"""

class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        """
        solution:
        (1) calculate all subarray sum of len L and M
        (2) for result from (1), get max value sequence
        (3) traversal one calculated subarray sum, with result (2), get result
        (4) [1,0,3]; 1,2; 4 
        """
        def get_subarray_sum(A, L):
            sum_l = []
            sum_ = sum(A[:L])
            sum_l.append(sum_)
            for i in range(L, len(A)):
                sum_ = sum_ + A[i] - A[i-L]
                sum_l.append(sum_)
            return sum_l
        
        def get_max_stack(p):
            max_ = -1
            max_m = [0] * len(p)
            # reverse, max: from right to left
            for i in xrange(len(p)-1, -1, -1):
                if p[i] > max_:
                    max_ = p[i]
                max_m[i] = max_
            return max_m
        
        def get_max_sum(sum_l, max_m, lenA, L, M):
            result = -1
            for i in xrange(len(sum_l)):
                ori_i = i + L - 1
                # point 
                m_i = ori_i + M - (M -1)
                if m_i < len(max_m):
                    result = max(result, sum_l[i]+max_m[m_i])
            return result
            
        result = -1
        if not A or L + M > len(A):
            return result
        # (1) calculate subarray sum with len L, M
        # from left to right -->
        sum_l = get_subarray_sum(A, L)
        sum_m = get_subarray_sum(A, M)
        # (2) calculate max value sequence
        # from right to left
        max_l = get_max_stack(sum_l)
        max_m = get_max_stack(sum_m)
        # (3) from (sum_l, max_m), (sum_m, max_l), get max of 2 sub array
        max_l_l = get_max_sum(sum_l, max_m, len(A), L, M)
        max_l_m = get_max_sum(sum_m, max_l, len(A), M, L)
        return max(max_l_l, max_l_m)
        

