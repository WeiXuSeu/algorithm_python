#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" 
while "AEC" is 

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        """
        solutin:
        f(i)(j): valide count in S[i] & T[j]
        if T[i] != S[j]
            f(i)(j) = f(i)(j-1)
        else:
            f(i)(j) = f(i)(j-1) + f(i-1)(j-1)
        if not T, S: 1
        if T and not S: 0
        """
        if not t:
            return 1
        if not s:
            return 0
        state = [[0]*(len(s)+1) for i in range(len(t)+1)]
        state[0] = [1]*(len(s)+1)
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    state[i+1][j+1] = state[i+1][j] + state[i][j]
                else:
                    state[i+1][j+1] = state[i+1][j]
        return state[len(t)][len(s)]