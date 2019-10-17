#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        if height is None or len(height) < 3:
            return result
        left = 0
        right = len(height) - 1
        left_max = right_max = 0
        # for index i: water = min{max_left(i), max_right(i)} - height(i)
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max <= right_max:
                result += left_max - height[left] 
                left += 1
            else:
                result += right_max - height[right]
                right -= 1
        return result