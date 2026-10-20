# Violet Gonzalez, Oct 20, 2026
# SWE 240P Assignment 2: Stack and Queue



# Task 1: Implement a stack data structure from scratch. 
# You can’t use built-in Stack APIs. You can use the built-in Array or 
# List or your custom-built LinkedList.  The Stack class must have the following 
# functions. Write sample test cases to validate your implementation.


class Stack:
    """ Stack is LIFO and built on the Python list. The end of the 
    list will be identified as the top """

    def __init__(self):
        self._elements = []

    def size(self):
        return len(self._elements)

    def is_empty(self):
         return self.size() == 0
    
    def push(self, element):
        """ Passes element to the lists append thus allowing
         it to add to the top """
        self._elements.append(element)

    def peek(self):
        """ Returns the last elements without removing it, raises IndexError when empty """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        else:
            return self._elements[-1]

    def pop(self):
        """ Calls the lists pop so the will be no recursion. It removes the and returns the top 
        Raises indexError when empty """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        else:
            return self._elements.pop()