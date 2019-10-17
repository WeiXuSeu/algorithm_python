
"""
Given n non-negative integers representing the histogram's bar height where the width 
of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution(object):
    def largestRectangleArea1(self, heights):
    	"""
    	method1: normal method
    	"""
        if heights is None:
            return
        
        max_area = 0
        for center in range(len(heights)):
            left_width = right_width = 0
            for left_index in range(center-1, -1, -1):
                if heights[left_index] >= heights[center]:
                    left_width += 1
                else:
                    break
            for right_index in range(center+1, len(heights), 1):
                if heights[right_index] >= heights[center]:
                    right_width += 1
                else:
                    break
            max_area = max(heights[center]*(left_width+right_width+1), max_area)
        return max_area
    

    def largestRectangleArea2(self, heights):
        """
        method2:
            (1) usally choose sub peak bar as right boundary,
                for the last bar, add 0 to right to make sure it will be treat as boundary;
            (2) 我们只需在这些局部峰值处进行处理，为啥不用在非局部峰值处统计呢，这是因为非局部峰值处的情况，后面的局部峰值都可以包括
        """
        heights.append(0)
        max_rec = 0
        stack = []
        for i in xrange(len(heights)):
            while(len(stack) > 0 and heights[stack[-1]] > heights[i]):
                top = stack.pop()
                height = heights[top]
                width = i - stack[-1] - 1 if len(stack) > 0 else i
                max_rec = max(max_rec, height * width)
            stack.append(i)
        return max_rec
            
            
            
            
            
            
            
            
            
            
            
            
        
            
