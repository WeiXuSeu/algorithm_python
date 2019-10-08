#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
978. Longest Turbulent Subarray
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
"""

class Solution(object):
    def maxTurbulenceSize0(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        keep state of each pair => 
            increase: True, 
            decrease: False, 
            equal/init: None 
        state_change: True->False, False->True, +1
        state not change: True->True, False->False, =2
        equal: =1, contine
        """
        if not A:
            return 0
        result = 1
        sub_sum = 1
        pre_state = None
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                state = True
            elif A[i] < A[i-1]:
                state = False
            else:
                sub_sum = 1
                state = None
                continue
            if state != pre_state:
                sub_sum += 1
            else:
                sub_sum = 2
            pre_state = state
            if sub_sum > result:
                result = sub_sum
        return result

    # Solution2
    def maxTurbulenceSize1(self, A):
    	pre = 0
    	cur = 0
    	result = 1
    	sub_len = 1
    	for i in range(1, len(A)):
    		cur = cmp(A[i], A[i-1])
    		# (+/-), (-/+) 抖动，与之前状态不同，满足条件，+1
    		if pre*cur < 0:
    			sub_len += 1
    		# 当前状态为0，重新开始，sub_len = 0
    		elif cur == 0:
    			sub_len = 1
    		# (++,--,0+,0-) 当前状态不为0，且前后状态之积不为-1
    		else:
    			sub_len = 2
    		cur = pre
    		result = max(result, sub_len)
    	return result




        
                