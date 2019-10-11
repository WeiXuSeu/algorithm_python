#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
930. Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?
Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,,]
[1,0,1,0,]
[,0,1,0,1]
[,,1,0,1]
"""

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        
        """
        solution1 
        (1) get prefix sum of array A: [0,1], [0,2], [0,3]
            [1, 0, 1, 0, 1] => [1, 1, 2, 2, 3]
        (2) subarray count related to: current_sum & pre_sum
        (3) for pre_sum 0 => init value 1; 
        """
        
        if not A:
            return 0
        current_sum = 0
        sum_dict = {}
        sum_dict[0] = 1
        count = 0
        for x in A:
            current_sum += x
            pre_sum = current_sum - S
            if pre_sum in sum_dict:
                count += sum_dict[pre_sum]
            if current_sum in sum_dict:
                sum_dict[current_sum] += 1
            else:
                sum_dict[current_sum] = 1
        return count