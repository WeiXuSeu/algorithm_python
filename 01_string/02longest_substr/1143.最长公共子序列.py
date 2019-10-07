#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters. 
(eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        """
        solution: longest common sub-sequence
        L(i,j) = L(i-1,j-1) + 1, (A[i]=B[j])
                 max(L(i, j-1), L(i-1,j)), (A[i]!=B[j]) 
        """
        test1 = text1
        test2 = text2
        if not test1 or not test2:
            return 0
        state = [[0]*(len(test2)+1) for _ in range(2)]
        for i in xrange(len(test1)):
            for j in xrange(len(test2)):
                if test1[i] == test2[j]:
                    state[i%2][j+1] = state[1-i%2][j] + 1
                else:
                    state[i%2][j+1] = max(state[1-i%2][j+1], state[i%2][j])
        return state[i%2][-1]
