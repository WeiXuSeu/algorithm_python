#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution:
    def strStr0(self, haystack, needle):
        """
        solution1: 遍历
        复杂度O(M*N)
        """
        
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        result = -1
        for i in range(len(haystack)-len(needle)+1):
            isExist = True
            for j in range(len(needle)):
                if needle[j] != haystack[j+i]:
                    isExist = False
                    break
            if isExist:
                result = i
                break
        return result
        
        
    """
    solution2: KMP
    """
        
    def strStr1(self, haystack, needle):
        def getNext(needle):
            """
            - 获取next数组
            - 前缀和后缀match的最大长度
              因为时前后缀，所以first, second index需要相邻，而不相等
            - next数组中,到了0,表示从字符开头重新的当前字符匹配，没有之前的余量（前后缀重叠）
                        到了-1,表示0处匹配都失败了，前进一个字符（+1）继续匹配
            """
            if not needle:
                return
            nextArr = [0] * len(needle)
            nextArr[0] = -1
            first = -1
            # index in main string
            second = 0 
            while second < len(needle)-1:
                if first == -1 or needle[first] == needle[second]:
                    """
                    重叠pattern的长度为first+1，对标的index为second+1(表示之前的match关系)
                    初始化时first为-1，满足预期；如果match失败，最终也会first为-1，对应值为变成0
                    """
                    first += 1
                    second += 1
                    nextArr[second] = first
                else:
                    """
                    str[0:first]重叠的pattern长度为nextArr[firt],所以需要更新索引为nextArr[first],
                    继续比较
                    """
                    first = nextArr[first]
            return nextArr
        
        ######main######
        if not needle:
            return 0
        if not haystack or len(haystack) < len(needle):
            return -1
        result = -1
        nextArr = getNext(needle)
        # 两字符串从起始位置开始匹配：0
        first = 0
        second = 0
        while second < len(haystack):
            if first == -1 or needle[first] == haystack[second]:
                first += 1
                second += 1
                if first == len(needle):
                    result = second - len(needle)
                    break
            else:
                first = nextArr[first]
        return result
