#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume 
that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        solution: 推到
        p[i,j]表示在区间[i,j]内的回文子序列长度
        则p[i-1,j+1] = max(p[i-1,j], p[i,j+1]) (if s[i-1] != s[j+1])
                       p[i,j] + 2              (if s[i-1] == s[j+1])
        p[i,i]=1, 只包含s[i]
        """
        if not s:
            return 0
        dp = [[0]*len(s) for _ in range(len(s))]
        result = 1
        for i in xrange(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, len(s)):
                if s[j] == s[i]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                if dp[i][j] > result:
                    result = dp[i][j]
        return result