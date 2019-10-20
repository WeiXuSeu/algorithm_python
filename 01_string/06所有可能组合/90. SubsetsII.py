#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        solution1:
        [4,4,4,1,4]
        [4,1], [1,4] is different
        """
        
        """
        solution1:
        [4,4,4,1,4]
        [4,1], [1,4] is same
        """
        if not nums:
            return []
        result = [[]]
        sorted_nums = sorted(nums)
        for x in sorted_nums:
            new_l = []
            for item in result:
                if not item:
                    new_l.append([x])
                else:
                    new_l.append(item+[x])
            result += new_l
        result_tuple_l = [tuple(item) for item in result]
        result_set = set(result_tuple_l)
        return [list(item) for item in result_set]


    def subsetsWithDup1(self, nums):
    	"""
		如果有重复的，只需考虑最近生成的以该字符结尾的子数组
		[a,c,c,c]
		[[]], [[],[a]], [[],[a],[c],[a,c]]
		第一个以c结尾的子数组个数与不含c的子数组数量相等（len）；
		连续的第二个以c结尾的子数组，只需考虑含一个c的（len）
		连续的第三个以c结尾的子数组，只需考虑含两个c的（len）
    	"""
    	result = [[]]
        if not nums:
            return result
        st_nums = sorted(nums)
        uniq_len = 0
        for i in range(len(st_nums)):
        	# 因为已经排过序，第一个或不等的就是唯一的元素
            if i == 0 or st_nums[i] != st_nums[i-1]:
                new = [x + [st_nums[i]] for x in result]
                result += new
                uniq_len = len(result)
            else:
                dup_len = uniq_len//2
                new = [x + [st_nums[i]] for x in result[-dup_len:]]
                result += new
        return result

