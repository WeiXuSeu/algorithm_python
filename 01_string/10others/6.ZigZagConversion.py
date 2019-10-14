#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        if not s:
            return result
        if numRows == 1:
            return s
        buckets = ["" for i in range(numRows)]
        # loop length is T, with two part [0, numRows), [numRows, 2*numRows-2)
        T = 2 * numRows - 2
        for i in xrange(len(s)):
            tmp = i % T
            if tmp < numRows:
                buckets[tmp] += s[i]
            else:
                buckets[T-tmp] += s[i]
        for str_item in buckets:
            result += str_item
        return result