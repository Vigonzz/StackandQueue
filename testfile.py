# Testing the task with unittest
import unittest
from stack_db import Stack


class TestStack(unittest.TestCase):

    # Testing the stack 
    def test_new_empty_stack(self):
        '''Testing for an empty stack = passes'''
        stack = Stack()
        self.assertEqual(0, stack.size())
        self.assertTrue(stack.is_empty())

    def test_pop_returns_last_pushed(self):
        '''Testing for pushing the elements in the stack and if it actually follows the LIFO principle'''
        diff_stack = Stack()
        diff_stack.push(1)
        diff_stack.push(2)
        diff_stack.push(3)
        self.assertEqual(3, diff_stack.pop())
        self.assertEqual(2, diff_stack.pop())
        self.assertEqual(1, diff_stack.pop())

    # assertRaises Tests
    def test_pop_raise_empty(self):
        raise_stack = Stack()
        with self.assertRaises(IndexError):
            raise_stack.pop()

    def test_peek_raise_empty(self):
        peek_stack = Stack()
        with self.assertRaises(IndexError):
            peek_stack.peek()





if __name__ == "__main__":
    unittest.main()