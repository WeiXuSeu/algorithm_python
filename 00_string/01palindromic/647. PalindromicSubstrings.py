#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    """
    solution1: 常规解法
    考虑每个回文字符串的长度可能为奇数，也可能为偶数
    """
  
    def countSubstrings0(self, s: str) -> int:
        count = 0
        if not s:
            return s
        end = len(s) - 1
        for i in range(len(s)):
            count += self.palindromicNum(s, i, i, end)
            count += self.palindromicNum(s, i, i+1, end)
        return count
            
    def palindromicNum(self, s, left, right, end):
        result = 0
        while left>=0 and right<=end:
            if s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            else:
                break
        return result
 
    
    """
    solution2: 马拉车算法
    （1）按照马拉车算法计算出每个改造后回文串的长度
    （2）通过回文串的长度，推导出对应的原始的回文串的组合数
    """
    
    def manacher(self, s):
        if not s:
            return
        ms = '#' + '#'.join(s) + '#'
        result = [0] * len(ms)
        center = 0
        right = 0
        radix = 0
        for i in range(len(ms)):
            if i < right:
                radix = min(result[2*center-i], right-i)
            else:
                radix = 1
            while i - radix >= 0 and i + radix <= len(ms)-1 and ms[i-radix] == ms[i+radix]:
                radix += 1
            result[i] = radix
            if i + radix > right:
                right = i + radix
                center = i
        return result
    
    def countSubstrings1(self, s: str) -> int:
        if not s:
            return 0
        result_manacher = self.manacher(s)
        result = 0
        #通过半径推导出对应的回文串的个数
        for x in result_manacher:
            result += x//2
        return result
