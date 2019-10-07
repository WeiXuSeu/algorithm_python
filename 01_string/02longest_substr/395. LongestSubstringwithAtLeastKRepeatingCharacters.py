#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        solution:
        遍历得到每次字母出现的次数，对于不满足条件的字母，则需要以该字母分裂字符串
        继续上述操作
        """
        if not s or len(s) < k:
            return 0
        if k <= 0:
            return len(s)
        result = 0
        process_queue = []
        process_queue.append(s)
        while process_queue:
            sub_s = process_queue.pop(0)
            if len(sub_s) >= k:
                states = {}
                for x in sub_s:
                    if x not in states:
                        states[x] = 1
                    else:
                        states[x] += 1
                bad_keys = set()
                for key, value in states.items():
                    if value < k:
                        bad_keys.add(key)
                if not bad_keys:
                    result = max(result, len(sub_s))
                    continue
                start = 0
                for i in range(len(sub_s)):
                    if sub_s[i] in bad_keys:
                        if i - start >= k:
                            process_queue.append(sub_s[start:i])
                        start = i + 1
                # check enpoint is not bad key, normal end len(sub_s)-1
                if sub_s[i] not in bad_keys:
                    if i - start + 1 >= k:
                        process_queue.append(sub_s[start:])
        return result
  
