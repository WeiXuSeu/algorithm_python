#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements 
in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
"""

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        solution: 滑动窗口
        start 表示窗口左侧
        multi = multi[start, i]
        当multi超过限制时，start需要右移
        每次计算以i结尾的满足条件的连续子数组的数目
        """
        if not nums:
            return
        result = 0
        multi = 1
        start = 0
        for i in xrange(len(nums)):
            multi = multi * nums[i]
            while multi >= k and start <= i:
                multi = multi/nums[start]
                start += 1
            if multi < k and start <= i:
                result += i-start+1
        return result

