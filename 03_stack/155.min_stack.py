#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack0(object):

    def __init__(self):
        # initialize your data structure here.
        self.stack = []
        self.min_stack = []

    def push(self, x):
        # :type x: int
        # :rtype: None
        if not self.stack:
            self.stack.append(x)
            self.min_stack.append(x)
        else:
            self.stack.append(x)
            min_value = min(self.min_stack[-1], x)
            self.min_stack.append(min_value)

    def pop(self):
        # :rtype: None
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        
    def top(self):
        # :rtype: int
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        # :rtype: int
        if self.min_stack:
            return self.min_stack[-1]
    
        
class MinStack1(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        import sys
        self.min = sys.maxint
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # when min value need to change, also keep previous min value before it
        # else just keep current value
        # case about "=" in if , about min value appear several times (pop)
        if x <= self.min:
            # keep previous min value
            self.stack.append(self.min)
            # update current min value
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        # when the poped value change min value, pop and recover to previous min value
        # else just pop top value
        # if min appear several times, keep two (<= in push), pop first, set to second, 
        # also min 
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()
        
        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min
    


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()