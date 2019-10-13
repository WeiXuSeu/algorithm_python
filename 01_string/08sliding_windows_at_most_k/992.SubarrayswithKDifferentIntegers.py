#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
992. Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray 
of A good if the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
"""

class Windows(object):
    def __init__(self):
        from collections import Counter
        self.counter = Counter()
        self.uniq = 0
        
    def add(self, x):
        self.counter[x] += 1
        if self.counter[x] == 1:
            self.uniq += 1
    
    def remove(self, x):
        self.counter[x] -= 1
        if self.counter[x] == 0:
            self.uniq -= 1
    

class Solution(object):
    def subarraysWithKDistinct0(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        
        """
        """
        solution1: traversal
        """
        
        if not A:
            return 0
        result = 0
        for i in range(len(A)):
            f_set = set()
            for j in range(i, len(A)):
                f_set.add(A[j])
                size = len(f_set)
                if size == K:
                    result += 1
                elif size > K:
                    break
            if len(f_set) < K:
                break
        return result
        

    def subarraysWithKDistinct1(self, A, K): 
        """
        solution2: two sliding windows
        for A[j], i1 <= i2 < j
        i2 is right most index meet: uniq(A[i2:j]) = K
        i1 is the left most index meet: uniq(A[i1:j]) = K
        so subarray end with A[j], valide subarray is len([i1:i2])
        botn i1 & i2 is increasing
        so [i, j] is uniq
        """
        
        if not A or len(A) < K:
            return 0
        windows1 = Windows()
        windows2 = Windows()
        result = left1 = left2 = 0
        for x in A:
            # add item to windows
            windows1.add(x)
            windows2.add(x)
            # point to i2 + 1 (right most + 1) (not meet)
            while windows2.uniq >= K:
                windows2.remove(A[left2])
                left2 += 1
            # point to i1 (left most) (defult 0 also meet)
            while windows1.uniq > K:
                windows1.remove(A[left1])
                left1 += 1
            result += left2 - left1
        return result
        
    
    def subarraysWithKDistinct2(self, A, K): 
        """
        solution3: f(distinct[K]) = f(at_most[K]) - f(at_most[K-1])
        for each A[j] find left most A[i] meet condition
            then for subarray end with A[j] f(at_most[K][Aj]) = j-i+1
        """
        def at_most_k(A, K):
            from collections import Counter
            counter = Counter()
            if not A or len(A) < K:
                return 0
            result = i = 0
            for j in range(len(A)):
                counter[A[j]] += 1
                if counter[A[j]] == 1:
                    K -= 1
                while K < 0:
                    counter[A[i]] -= 1
                    if counter[A[i]] == 0:
                        K += 1
                    i += 1
                result += j - i + 1
            return result
        
        return at_most_k(A, K) - at_most_k(A, K-1)
        
        
        
        
        
        
        
        
        
            
                
