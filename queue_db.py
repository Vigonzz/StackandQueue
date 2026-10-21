# Violet Gonzalez, Oct 20, 2026
# SWE 240P Assignment 2: Stack and Queue

# Task 3: 
# Implement a Queue data structure from scratch. You cannot use built-in Queue APIs. 
# You can use the built-in Array or List or your custom-built LinkedList.  The Queue 
# class must have the following functions. Write sample test cases to validate your implementation.


# I am going to build my own linked list, this will keep the speed at o(1) and allow me to better understand the implementation of linked list better

class Node:
    ''' Node class for the nodes in our queue'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    ''' Queue is a data structure that follow the FIFO principle. The top is the end and the end is the tail '''

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter_size = 0

    def size(self):
        return self.counter_size
    
    def is_empty(self):
         return self.size() == 0
    
    def enqueue(self, element):
        ''' Adds a new node to the end of the tail and then claims the tail position'''
        starting = Node(element)

        if self.is_empty():
            self.head = starting
            self.tail = starting
        else:
            self.tail.next = starting
            self.tail = starting
        
        self.counter_size += 1

    def poll(self):
        ''' Returns the front value without removing it'''
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.head.value
        
    def dequeue(self):
        ''' Removes the head and reassigns it (only happens if a new node is added)'''
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            heads_value = self.head.value
            self.head = self.head.next
            self.counter_size -= 1

            if self.is_empty():
                self.tail = None

            return heads_value