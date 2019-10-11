#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer 
which has exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        solution:
        (1) 将每个位拆解为数列, 从左到右，位数递增
        (2) 从左至右，找到一个最近的导致下降的元素
        (3) 在下降元素之前的序列中，找到最小的比它大的值，交换位置
            则交换万后，下降元素之前仍为递增序列，需要把它反转为递减序列
            
        case1: in    1999999999
              out   9199999999
              except -1

        case2: 2365421 --> 2 4 65 3 21 --> 24 12356
        """
        import sys
        # MAX_INT = sys.maxint
        MAX_INT = 2147483647
        if n <= 0:
            return -1
        digit_list = []
        x = n
        while x:
            digit_list.append(x%10)
            x = x/10
        # 寻找下降元素
        incr_list = []
        is_exist = False
        for i in xrange(len(digit_list)):
            if incr_list and digit_list[i] < incr_list[-1]:
                is_exist = True
                for j in xrange(len(incr_list)):
                    if incr_list[j] > digit_list[i]:
                        break
                tmp = digit_list[i]
                digit_list[i] = incr_list[j]
                incr_list[j] = tmp
            if is_exist:
                break
            incr_list.append(digit_list[i])
        if not is_exist:
            return -1
        incr_list.reverse()
        target_list = incr_list + digit_list[i:]
        result = 0
        for i in xrange(len(target_list)-1, -1, -1):
            result = result*10 + target_list[i]
        if result > MAX_INT:
            return -1
        return result
        
