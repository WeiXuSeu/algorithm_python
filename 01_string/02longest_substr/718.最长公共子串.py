#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
718. MaximumLengthofRepeatedSubarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        """
        solution1: dp
        我们使用dp[i][j]表示 以x[i]和y[j]结尾的最长公共子串的长度，
        因为要求子串连续，所以对于X[i]与Y[j]来讲，它们要么与之前的公共子串构成新的公共子串；
        要么就是不构成公共子串。故状态转移方程为：
			X[i] == Y[j]，dp[i][j] = dp[i-1][j-1] + 1
            X[i] != Y[j]，dp[i][j] = 0
		对于初始化，i==0或者j==0，如果X[i] == Y[j]，dp[i][j] = 1；否则dp[i][j] = 0。
        """

        if not A or not B:
            return 0
        states = [[0]*(len(B)+1) for i in range(2)]
        result = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    states[i%2][j+1] = states[1-i%2][j] + 1
                    result = max(result, states[i%2][j+1])
                else:
                    states[i%2][j+1] = 0
        return result