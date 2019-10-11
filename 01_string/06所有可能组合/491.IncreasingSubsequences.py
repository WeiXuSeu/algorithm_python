#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
491. Increasing Subsequences

Given an integer array, your task is to find all the different possible 
increasing subsequences of the given array, and the length of an 
increasing subsequence should be at least 2.

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also 
be considered as a special case of increasing sequence.
"""

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        """
        solution: iteration solution
        组合所有的子序列
        从空子序列开始构造出所有的子序列组合
        """
        if not nums or len(nums)<2:
            return []
        
        result_list = [[]]
        for x in nums:
            new_ = []
            for item in result_list:
                if not item:
                    new_.append([x])
                else:
                    if x >= item[-1]:
                        new_.append(item+[x])
            result_list = result_list + new_
        result_tuple_l  = [tuple(item) for item in result_list if len(item)>=2]
        result_set = set(result_tuple_l)
        return [list(item) for item in result_set]