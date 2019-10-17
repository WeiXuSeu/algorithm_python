#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_queue = []
        self.pop_queue = []
    
    # at one time, one queue is empty
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        while self.pop_queue:
            top = self.pop_queue.pop()
            self.push_queue.append(top)
        self.push_queue.append(x)
        
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.pop_queue:
            return self.pop_queue.pop(0)
        else:
            while self.push_queue:
                top = self.push_queue.pop() 
                self.pop_queue.append(top)
            if self.pop_queue:
                return self.pop_queue.pop(0)
                
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.pop_queue:
            return self.pop_queue[0]
        else:
            while self.push_queue:
                top = self.push_queue.pop()
                self.pop_queue.append(top)
            if self.pop_queue:
                return self.pop_queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.pop_queue and not self.push_queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()