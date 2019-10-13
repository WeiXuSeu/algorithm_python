#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that 
if you only sort this subarray in ascending order, then the whole array 
will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to 
make the whole array sorted in ascending order.
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        solution1: sort & compare
        """
        """
        if not nums:
            return 0
        start = -1
        end = -1
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] != nums[i]:
                start = i
                break
        if start == -1:
            return 0
        for i in range(len(nums)-1, -1, -1):
            if sorted_nums[i] != nums[i]:
                end = i
                break
        return end-start+1
        """
        
        """
        solution2: 
        (1) from left, find max value, if x[i] < max, then i is end in [0, i]
        (2) from right, find min value, if x[i] > min, the i is begin in [i, len-1]
        """
        import sys
        MAX = -sys.maxint - 1
        MIN = sys.maxint
        start = -1
        end = -1
        if not nums:
            return 0
        size = len(nums)
        for i in range(size):
            # from left to right
            MAX = max(MAX, nums[i])
            if nums[i] < MAX:
                end = i
            # from right to left
            MIN = min(MIN, nums[size-1-i])  
            if nums[size-1-i] > MIN:
                start = size-1-i
                
        if start == -1:
            return 0
        return end-start+1
            
            
        

