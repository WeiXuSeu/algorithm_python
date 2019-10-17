#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given a string s that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:

Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
"""

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        solution:
        case: abc()def(((mq)))
        遇到")",则反转对应的"()",并弹出"("
        """
        if not s:
            return s
        result = []
        reverse = []
        for i in xrange(len(s)):
            if s[i] == ")":
                x = result.pop()
                while x != "(":
                    reverse.append(x)
                    x = result.pop()
                result += reverse
                reverse = []
            else:
                result.append(s[i])
        return "".join(result)