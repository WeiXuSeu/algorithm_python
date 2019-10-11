#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
974. Subarray Sums Divisible by K

Given an array A of integers, 
return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""

class Solution(object):
    def subarraysDivByK0(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        """
        solution1:
            traversal each subarry
            time limited
        """
        
        count = 0
        if not A:
            return 0
        for i in range(len(A)):
            sum_array = 0
            for j in range(i, len(A)):
                sum_array += A[j]
                if sum_array % K == 0:
                    count += 1
        return count
        

    def subarraysDivByK1(self, A, K):
        """
        solution2: 
        calculate sum from 0: (0,1), (0,2), (0,3), ...
        mark each sub_sum by mod_value, for K, its mod_value is (0, 1, 2, ..., mod-1)
        for mod_val: 0, its initail value is 1, when meet, each is valid
        for others: its initail value is 0, when meet twice, valid times 1; meet triple, valide times 2;
        """
        if not A:
            return 0
        mod_dict = {}
        mod_dict[0]=1
        sum_value = 0
        count = 0
        for i in range(len(A)):
            sum_value += A[i]
            mod_value = sum_value % K
            if mod_value in mod_dict:
                # for valide subarray end with i, times: mod_dict[mod_value]
                count += mod_dict[mod_value]
                mod_dict[mod_value] += 1
            else:
                # mod_value first meet, init to 1
                mod_dict[mod_value] = 1
        return count