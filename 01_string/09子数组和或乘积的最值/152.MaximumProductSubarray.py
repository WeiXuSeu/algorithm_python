#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        solution:
        当nums中不含0时，nums[0:i]的乘积的绝对值是单调递增的，
            若累乘的最后一个数为正数，则肯定为最大值;
            若累乘的最后一个数为负数，
                若负数只出现一次，即最后一个，不用处理；
                若出现多次，则只需最后一次除第一次出现的负数（最左）
                    含偶数个负数的话，最后一个累积，定为正
                    含奇数个负数的话，排除最右侧的负数，已在之前的遍历中
                        只需考虑排序最左侧的一个负数
        当nums中含0时，从0处分段
        """
        import sys
        if not nums:
            return
        meet_minu = False
        val_minu = None
        num_minu = 0
        multi = 1
        result = -sys.maxint-1
        for x in nums:
            if x == 0:
                if multi < 0 and num_minu > 1:
                    result = max(result, multi/val_minu)
                result = max(result, 0)
                num_minu = 0
                multi = 1
            else:
                multi *= x
                if multi < 0:
                    if num_minu == 0:
                        val_minu = multi
                    num_minu += 1
                result = max(result, multi)
        if multi < 0 and num_minu > 1:
            result = max(result, multi/val_minu)
        return result
