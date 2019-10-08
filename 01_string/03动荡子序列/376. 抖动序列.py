#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
376. Wiggle Subsequence

A sequence of numbers is called a wiggle sequence if the differences between successive numbers 
strictly alternate between positive and negative. The first difference (if one exists) may be 
either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
"""

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
    	"""
    	在每一次状态变化时，序列+1
    	(1) 初始或中间某个状态为0，之后状态变化， 0 ---> !0  (+1)
    	(2) ++-,++0++- (+1)
    	"""
        if not nums:
            return 0
        result = 1
        pre_state = 0
        for i in range(1, len(nums)):
            state = nums[i] - nums[i-1]
            if state > 0:
                state = 1
            elif state < 0:
                state = -1
            if state == 0:
                continue
            elif state != pre_state:
                result += 1
                pre_state = state
        return result