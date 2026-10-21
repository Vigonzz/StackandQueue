# Testing the task with unittest
import unittest
from queue_db import *


class TestQueue(unittest.TestCase):
    

    def test_queue_empty(self):
        ''' Testing for an empty queue '''
        queue = Queue()

        self.assertEqual(0, queue.size())
        self.assertTrue(queue.is_empty())

    def test_enqueue_increase(self):
        ''' Testing for enqueue elements to the queue '''
        enqueue_increase = Queue()

        enqueue_increase.enqueue(1)
        enqueue_increase.enqueue(2)
        enqueue_increase.enqueue(3)
        
        self.assertEqual(3, enqueue_increase.size())
        self.assertFalse(enqueue_increase.is_empty())

    def test_dequeue_order(self):
        ''' Testing that queue is following the FIFO principle '''
        dequeue_order = Queue()

        dequeue_order.enqueue(10)
        dequeue_order.enqueue(20)
        dequeue_order.enqueue(30)

        self.assertEqual(10, dequeue_order.dequeue())
        self.assertEqual(20, dequeue_order.dequeue())
        self.assertEqual(30, dequeue_order.dequeue())

    def test_poll_front(self):
        ''' Test to ensure that poll is returning the front of th chain '''
        poll_front = Queue()

        poll_front.enqueue(30)
        poll_front.enqueue(40)
        poll_front.enqueue(50)

        self.assertEqual(30, poll_front.poll())

    def test_poll_not_remove(self):
        ''' Testing to ensure poll does not remove a node '''
        poll_not_remove = Queue()

        poll_not_remove.enqueue(50)
        self.assertEqual(1, poll_not_remove.size())

        poll_not_remove.enqueue(60)
        self.assertEqual(2, poll_not_remove.size())

    def test_dequeue_empty(self):
        ''' Test for using dequeue on empty stack it should return an indexError '''
        dequeue_raise = Queue()

        with self.assertRaises(IndexError):
            dequeue_raise.dequeue()
    
    def test_poll_empty(self):
        ''' Test to ensure that poll does not work on an empty queue, it should raise an indexError '''
        poll_raise = Queue()

        with self.assertRaises(IndexError):
            poll_raise.poll()
        
    def test_empty_reuse(self):
        ''' Test to see if the queue can be built, emptied, and then reused '''
        empty_reuse = Queue()

        empty_reuse.enqueue(12)
        empty_reuse.enqueue(13)
        empty_reuse.enqueue(14)

        self.assertEqual(12, empty_reuse.dequeue())
        self.assertEqual(13, empty_reuse.dequeue())
        self.assertEqual(14, empty_reuse.dequeue())

        self.assertTrue(empty_reuse.is_empty())

        empty_reuse.enqueue(15)
        empty_reuse.enqueue(16)
        empty_reuse.enqueue(17)

        self.assertEqual(15, empty_reuse.poll())
        self.assertEqual(3, empty_reuse.size())

    def test_interleaved_ops(self):
        ''' Test for interleaved operations '''
        interleaved_queue = Queue()

        interleaved_queue.enqueue(2)
        interleaved_queue.enqueue(3)
        self.assertEqual(2, interleaved_queue.dequeue())
        self.assertEqual(3, interleaved_queue.poll())

        
        interleaved_queue.enqueue(4)
        self.assertEqual(3, interleaved_queue.dequeue())
        self.assertEqual(4, interleaved_queue.poll())
        self.assertEqual(4, interleaved_queue.dequeue())

    def test_mixed_types(self):
        ''' Test different data types '''
        mixed_stack = Queue()

        mixed_stack.enqueue("Very tired")
        mixed_stack.enqueue(43)
        mixed_stack.enqueue([6,8])

        self.assertEqual("Very tired", mixed_stack.dequeue())
        self.assertEqual(43, mixed_stack.dequeue())
        self.assertEqual([6,8], mixed_stack.dequeue())


if __name__ == "__main__":
    unittest.main()