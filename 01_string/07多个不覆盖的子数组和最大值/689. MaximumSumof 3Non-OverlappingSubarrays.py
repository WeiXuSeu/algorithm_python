#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
Return the result as a list of indices representing the starting position of each interval 
(0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

[1,2,1,2,1,2,1,2,1] 2
[0,2,4] 
[0,2,7]也满足结果一样，但是不满足lexicographically smallest one.
"""

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        """
        solution1: 
        (1) calculate all subarray with width: k
        (2) find three items in sum_array with interval (at least k)
        (3) for nums[i, j, k]
            fixed j, the we need to find
            first appearance of max value in [0, j-k]
            first appearance of max value in [j+k, end]
        (4) we need to construct:
            left(x): first appearance of max value in [0, x]
            right(x): first appearance of max value in [x, end]
        """
        if not nums or k <=0 or len(nums) < 3*k:
            return
        
        # calculate sum_array
        w = [0] * (len(nums)-k+1)
        sum_ = 0
        for i in range(k):
            sum_ += nums[i]
        w[0] = sum_
        for i in range(k, len(nums)):
            w[i-k+1] = w[i-k] + nums[i] - nums[i-k]
        
        # calculate left(x)
        left = [0] * len(w)
        best = 0
        for i in range(0, len(w)):
            if w[i] > w[best]:
                best = i
            left[i] = best
        # calculate right(x)
        right = [0] * len(w)
        best = len(w)-1
        for i in range(len(w)-1, -1, -1):
        	# lexicographically smallest
            if w[i] >= w[best]:
                best = i
            right[i] = best
        
        # given j: calculate W[i] + W[j] + W[k] & i+j+k
        max_value = 0
        min_index = []
        tmp_dict = {}
        for j in range(k, len(w)-k):
            value = w[left[j-k]] + w[j] + w[right[j+k]]
            if value > max_value:
                max_value = value
                min_index = [left[j-k], j, right[j+k]]
        return min_index
                


