#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1044. Longest Duplicate Substring

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""

class Solution(object):
    def longestDupSubstring0(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        solution1: 利用后缀数组求解
        （1）找到所有的后缀数组
        （2）对后缀数组排序
        （3）求相邻后缀数组的最长公共字串LCS
        Memory Limit Exceeded
        """
        
        def common_str(S, P):
            count = 0
            lens = min(len(S), len(P))
            for i in xrange(lens):
                if P[i] == S[i]:
                    count += 1
                else:
                    break
            return count
        
        #### main func ####
        if not S or len(S) < 2:
            return 0
        
        suffix_arr = [S[i:] for i in range(len(S))]
        sorted_suffix = sorted(suffix_arr)
        index = None
        max_c = 0
        result = ""
        for i in xrange(len(sorted_suffix)-1):
            count = common_str(sorted_suffix[i], sorted_suffix[i+1])
            if count > max_c:
                index = i
                max_c = count
        if index is not None:
            result = sorted_suffix[index][0:max_c]
        return result

    def longestDupSubstring1(self, S):
        """
        solution2:
        (1) 采用二分法，指定需要比较的字串的长度
        (2) 可以将字符串转化为base=26的整数，则比较字符串即相当于比较整数，O(n) -> O(1)
            采用rolling hash的方式，利用之前计算的结果
        """
        mod = 2**63 - 1
        
        def lds(A, L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in xrange(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        
        if not S or len(S) < 2:
            return 0
        old_S = S
        S = [ord(x) - ord('a') for x in S]
        start = 0
        end = len(S) - 1
        result = ""
        result_len = 0
        while start < end:
            mid = (start+end)/2
            index = lds(S, mid+1)
            if index is None:
                end = mid - 1
            else:
                result = index
                result_len = mid+1
                start = mid
        if result:
            result = old_S[result:result+result_len]
        return result
        
    def longestDupSubstring2(self, S):
        """
        solition3
        """
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in xrange(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        
        """
        以下为二分查找找到相应index的方法，test函数所需参数为相应的长度，故+1
        """
        res, lo, hi = 0, 0, len(S) - 1
        while lo <= hi:
            mi = (lo + hi) / 2
            pos = test(mi+1)
            if pos:
            	# length & postion
                lo = mi + 1
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
