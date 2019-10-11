#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        solution: 
        通过累计和的方式，以空间换时间
        每次计算sum[i]时，看sum[i]-k是否存在，若存在，即是sum[i]-k出现的次数（以i结尾）
        """
        if not nums:
            return
        states = {}
        states[0] = 1
        sum_ = 0
        count = 0
        for x in nums:
            sum_ += x
            # 先获取满足条件的数目，再更新当下状态，当 x ==0 （k==0）时成立；若先更新当下状态则不成立
            if sum_ - k in states:
                count += states[sum_ - k]
            if sum_ in states:
                states[sum_] += 1
            else:
                states[sum_] = 1
        return count