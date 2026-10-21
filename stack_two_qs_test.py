# Testing the task with unittest

# The same test case as the testfile (task 1) since we are using a stack (just with queue within it)
import unittest
from stack_two_queues import *

class TestStackWithTwoQueues(unittest.TestCase):
     # Testing the stack 
    def test_new_empty_stack(self):
        '''Testing for an empty stack = passes'''
        stack = StackWithTwoQues()

        self.assertEqual(0, stack.size())
        self.assertTrue(stack.is_empty())

    def test_pop_returns_last_pushed(self):
        '''Testing for pushing the elements in the stack and if it actually follows the LIFO principle'''
        diff_stack = StackWithTwoQues()

        diff_stack.push(1)
        diff_stack.push(2)
        diff_stack.push(3)

        self.assertEqual(3, diff_stack.pop())
        self.assertEqual(2, diff_stack.pop())
        self.assertEqual(1, diff_stack.pop())

    # assertRaises Tests
    def test_pop_raise_empty(self):
        '''Test for popping on an empty stack should raise an IndexError'''
        raise_stack = StackWithTwoQues()

        with self.assertRaises(IndexError):
            raise_stack.pop()

    def test_peek_raise_empty(self):
        '''Test for using peek on an empty stack, it should raise an indexError'''
        peek_stack = StackWithTwoQues()

        with self.assertRaises(IndexError):
            peek_stack.peek()

    def test_push_increase_size(self):
        '''Test for pushing elements to the stack and check size'''
        push_stack = StackWithTwoQues()

        push_stack.push(1)
        push_stack.push(2)
        push_stack.push(3)

        self.assertEqual(3, push_stack.size())
        self.assertFalse(push_stack.is_empty())

    def test_peek_return_top(self):
        '''Test for peek to return the top of stack'''
        peek_return_stack = StackWithTwoQues()

        peek_return_stack.push(1)
        peek_return_stack.push(2)
        peek_return_stack.push(3)

        self.assertEqual(3, peek_return_stack.peek())

    def test_peek_not_remove(self):
        ''' Test for peek on stack, no removing'''
        peek_not_remove = StackWithTwoQues()

        peek_not_remove.push(10)
        peek_not_remove.push(20)
        peek_not_remove.push(30)

        self.assertEqual(30, peek_not_remove.peek())
        self.assertEqual(30, peek_not_remove.peek())
        self.assertEqual(3, peek_not_remove.size())

    def test_reuse_empty(self):
        '''Test reusing the stack from empty'''
        reuse_stack = StackWithTwoQues()

        reuse_stack.push(40)
        reuse_stack.push(50)
        reuse_stack.push(60)

        self.assertEqual(60, reuse_stack.pop())
        self.assertEqual(50, reuse_stack.pop())
        self.assertEqual(40, reuse_stack.pop())

        self.assertTrue(reuse_stack.is_empty())

        reuse_stack.push(70)
        reuse_stack.push(80)
        reuse_stack.push(90)

        self.assertEqual(90, reuse_stack.peek())
        self.assertEqual(3, reuse_stack.size())

    def test_mixed_types(self):
        '''Test different typed in the stack'''
        mixed_stack = StackWithTwoQues()

        mixed_stack.push("Tired")
        mixed_stack.push(40)
        mixed_stack.push([1,2])

        self.assertEqual([1,2], mixed_stack.pop())
        self.assertEqual(40, mixed_stack.pop())
        self.assertEqual("Tired", mixed_stack.pop())

    def test_longer_sequence(self):
        ''' Test a longer sequence to see if it behaves as expected '''
        longer_sequence = StackWithTwoQues()

        longer_sequence.push(1)
        longer_sequence.push(2)
        longer_sequence.push(3)
        longer_sequence.push(4)
        longer_sequence.push(5)

        self.assertEqual(5, longer_sequence.pop())
        self.assertEqual(4, longer_sequence.pop())

        longer_sequence.push(6)
        longer_sequence.push(7)

        self.assertEqual(7, longer_sequence.pop())
        self.assertEqual(6, longer_sequence.pop())
        self.assertEqual(3, longer_sequence.pop())
        self.assertEqual(2, longer_sequence.pop())
        self.assertEqual(1, longer_sequence.pop())

        self.assertTrue(longer_sequence.is_empty())


if __name__ == "__main__":
    unittest.main()