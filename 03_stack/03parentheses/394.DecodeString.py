#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square 
brackets is being repeated exactly k times. Note that k is guaranteed to be a positive 
integer.

You may assume that the input string is always valid; No extra white spaces, square 
brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and 
that digits are only for those repeat numbers, k. For example, there won't be input like 
3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_str = ""
        curr_num = 0
        # get string and number before [, use them when meet ]
        for x in s:
            if x == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0
            elif x == "]":
                num = stack.pop()
                pre_str = stack.pop()
                curr_str = pre_str + num * curr_str
            elif x.isdigit():
                curr_num = 10*curr_num + int(x)
            else:
                curr_str += x
        return curr_str
            
        