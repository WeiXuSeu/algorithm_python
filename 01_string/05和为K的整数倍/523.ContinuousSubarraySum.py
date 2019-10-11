#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
523. Continuous Subarray Sum

Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 
that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        """
        solution1: iterate nums, calculate sum[i] = sum[0:i+1] contain 0-i
        if sum[i]%k appareded before, it's true 
        
        special cases: (1) [0,0] k=0 True
                       (2) [1,0] k=2 False
                       (3) [0,0] k=-1 True
                       (4) [5,0,0] k=0 True
                       (5) [1,2,12], k=6, False
                       (6) [0,1,0], k=-1, True
        """
        
        if not nums or len(nums) < 2:
            return False
        sum_ = 0
        states = {}
        states[0] = -1
        result = False
        for i in xrange(len(nums)):
            # (1) if [0,0] exist, true, 0 *k
            if i > 0 and nums[i-1] == 0 and nums[i] == 0:
                return True
            sum_ += nums[i]
            
            if k!=0:
                """
                if mod == 0, true if index!=0
                if mod !=0, mod[index1] = mod[index2] and index2 - index1 > 1
                for index --> mod, keep smallest index
                """
                mod = sum_ % k 
                if mod in states:
                    if i - states[mod] > 1:
                        return True
                else:
                    states[mod] = i
        return result
        
