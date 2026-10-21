# Violet Gonzalez, Oct 20, 2026
# SWE 240P Assignment 2: Stack and Queue



# Task 1: Implement a stack data structure from scratch. 
# You can’t use built-in Stack APIs. You can use the built-in Array or 
# List or your custom-built LinkedList.  The Stack class must have the following 
# functions. Write sample test cases to validate your implementation.


# To better understand stack, I read more documentation:
# GeeksforGeeks. (2026, May 19). Stack in python. https://www.geeksforgeeks.org/python/stack-in-python/ 


class Stack:
    """ Stack is LIFO and built on the Python list. The end of the 
    list will be identified as the top """

    # I kept getting mixed up on objects overall, this helped a bit:
    # 3. data model. Python documentation. (n.d.-a). https://docs.python.org/3/reference/datamodel.html 

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
        # Read and saw examples for accessing elements for the end of the sequence:
        # GeeksforGeeks. (2026c, October 1). What is negative indexing in Python? https://www.geeksforgeeks.org/python/what-is-negative-indexing-in-python/ 

        if self.is_empty():
            raise IndexError("Peek from empty stack")
        else:
            return self._elements[-1]

    def pop(self):
        """ Removes the element and returns the top 
        Raises indexError when empty """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        else:
            return self._elements.pop()