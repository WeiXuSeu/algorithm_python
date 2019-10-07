#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    """
    Solution1: travel the string, check each possibel substring
    for palindrom: its length may be even or odd
    """

    def findPalindrome(self, s, center_l, center_r):
        while center_l >= 0 and center_r < len(s) and s[center_l] == s[center_r]:
            center_l -= 1
            center_r += 1
        return s[center_l + 1:center_r]

    def longestPalindrome0(self, s):
        # :type s: str
        # :rtype: str
        result = ""
        if not s:
            return result
        for i in range(0, len(s)):
            # odd case, like "aba"
            target = self.findPalindrome(s, i, i)
            if len(target) > len(result):
                result = target
            # even case, like "abba"
            target = self.findPalindrome(s, i, i+1)
            if len(target) > len(result):
                result = target
        return result
            

    """
    Solution2: travel the string, check each possibel substring
    for palindrom: its length may be even or odd
    """
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        if not s:
            return result
        str_list = [x for x in s]
        str1 = "#" + "#".join(str_list) + "#"
        center = 0 # center of palindrome
        rmax = 0 # right boundary of palindrome (not include)
        d = [0] * len(str1) # radiux of the palindrome
        max_d = 0
        center_target = 0
        for i in range(0, len(str1)):
            """
            i < rmax:
                if d[2*center-i] < rmax-i:
                    d[i] = d[2*center-i]
                else:
                    let d[i] = rmax - i 
                    (which we can make sure, 
                     try to extend it later from this place with radiux d[i])
            else:
                d[i] = 1 
                (which we can make sure, 
                 try to extend it later from this place with radiux d[i])
            """
            d[i] = min(d[2*center - i], rmax-i) if i < rmax else 1
            while i - d[i] >=0 and i + d[i] < len(str1) and str1[i-d[i]] == str1[i+d[i]]:
                d[i] += 1
            # find target with max radiux
            if d[i] > max_d:
                max_d = d[i]
                center_target = i
            """
            update right most palindrome (tag by rmax)
            try to make item < rmax, find the largest rmax
            center is not the problem, always center<=i (i is a update value)
            """
            if i + d[i] > rmax:
                rmax = i + d[i]
                center = i
        result = str1[center_target - max_d + 1:center_target + max_d]
        result = result.replace("#","")
        return result