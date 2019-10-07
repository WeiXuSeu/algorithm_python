#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	"""
    	solution1: 动态规划
    	index_dict is state
            if s[i] in index_dict, we can get its position: index_dict[s[i]].
            if its position in invalid range [0, start), 
                s[i] is valide, add it to candidate sub str;
            if its position in valid range (>= start), cadidate sub str will be shorter
                update it with: index_dict[s[i]] + 1
            
            we keept all uniq elements(<=26 limit) in dict, 
            so position maybe (<start) or (>=start)
    	"""
        if not s:
            return 0
        state = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in state and state[s[i]] >= start:
                start = state[s[i]] + 1
            max_len = max(max_len, i - start + 1)
            state[s[i]] = i
        return max_len