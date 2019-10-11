#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
940. Distinct Subsequences II

Given a string S, count the number of distinct, non-empty subsequences of S .
Since the result may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".

Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
"""

class Solution(object):
    def distinctSubseqII0(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        solution1: 构造所有的可能子序列
        复杂度： O(N2)
        """
        if not S:
            return 0
        result = set([''])
        for x in S:
            new_str = set()
            for item in result:
                new_str.add(item+x)
            for item in new_str:
                if item not in result:
                    result.add(item)
        return len(result)-1
        
    def distinctSubseqII1(self, S):
        """
        solution2: 
        end[c]标记所有以‘c’结尾的子序列 (跟顺序无关)
        若‘c’在之前的序列里没出现过，则加 end[c] = sum[end] + 1; c为新增项
        若‘c’在之前的序列里出现过，end[c] = sum[end] + 1，替换掉之前的项，
            因为c与其他项的组合，包含之前以c结尾的项
        一个c结尾的组合数，多个c结尾的组合数
        """
        if not S:
            return 0
        end = [0] * 26
        mod = 10**9 + 7
        for x in S:
            end[ord(x) - ord('a')] = sum(end) + 1
        return sum(end) % mod
            
        
        
        
        
     
      