# Violet Gonzalez, Oct 21, 2026
# SWE 240P Assignment 2: Stack and Queue

# Task 4:
# Implement a Stack using only two instances of your 
# implemented Queue class (Task-3).  Write sample test cases to 
# validate your implementation.

from queue_db import Queue

class StackWithTwoQues:

    def __init__(self):
        ''' Create Two Queue objects '''
        self.queue_one = Queue()
        self.queue_two = Queue()

    def size(self):
        ''' Return the size of the queue holding the elements'''
        return self.queue_one.size()

    def is_empty(self):
        return self.size() == 0
    
    def push(self, x):
        ''' Have elements swap into queue two from queue one '''
        self.queue_two.enqueue(x)
        
        while not self.queue_one.is_empty():
           self.queue_two.enqueue(self.queue_one.dequeue())

        self.queue_one, self.queue_two = self.queue_two, self.queue_one

    def pop(self):
        ''' Removed the element and returns the most recently pushed element, will raise IndexError if empty '''
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        else:
            return self.queue_one.dequeue()
        
    def peek(self):
        ''' Returns the most recently pushed element(top) without removing it Will raise an IndexError if it is empty '''
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        else:
            return self.queue_one.poll()
        
        
    
