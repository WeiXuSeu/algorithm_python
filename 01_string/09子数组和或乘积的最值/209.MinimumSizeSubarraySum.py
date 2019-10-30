#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which 
the time complexity is O(n log n). 
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        solution: 滑动窗口
        """
        
        if not s:
            return 0
        mini_len = sys.maxint
        start = 0
        sum_ = 0
        for i in xrange(len(nums)):
            sum_ += nums[i]
            while sum_ >= s and i>=start:
                # 在缩小的过程中，可能碰见其他符合条件的
                if sum_ >= s:
                    mini_len = min(mini_len, i-start+1)
                sum_ -= nums[start]
                start += 1
        result = 0
        if mini_len != sys.maxint:
            result = mini_len
        return result
        