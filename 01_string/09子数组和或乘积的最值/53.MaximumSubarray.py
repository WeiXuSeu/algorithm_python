#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        solution1:
        f(n) = a[n] + f(n-1), (if f(n-1)>0)
        f(n) = a[n],          (if f(n-1)<=0)
        f(0) = a[0]
        """
        import sys
        if not nums:
            return
        sum_nums = nums[0]
        result = nums[0]
        for x in nums[1:]:
            if sum_nums > 0:
                sum_nums += x
            else:
                sum_nums = x
            if sum_nums > result:
                result = sum_nums
        return result
       