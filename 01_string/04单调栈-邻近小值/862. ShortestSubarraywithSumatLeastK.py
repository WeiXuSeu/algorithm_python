#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3

Case4:
[84,-37,32,40,95] K = 167
Output: 3

按照求最大子数组和的方式有问题的一点是[0:]满足条件，再从左侧递减时，减去84就不满足条件，需要同时减去[84,-37]
"""