# Last In, First Out..

# is_empty
# push
# peek
# is_full
# pop

import unittest

from stack.stack import Stack



class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_if_stack_is_empty_on_initialization(self):
        self.assertEqual(len(self.stack.items), 0)

    def test_items_gets_added_to_stack(self):
        self.stack.push('hello')
        self.assertEqual(len(self.stack.items), 1)
        self.assertEqual(self.stack.items[0], 'hello')

    def test_shows_the_last_item_on_peek(self):
        self.stack.push('hello')
        last_item = self.stack.peek()
        self.assertEqual(last_item, 'hello')

    def test_returns_false_when_stack_limit_is_not_reached(self):
        self.assertFalse(self.stack.is_full())

    def test_returns_true_when_stack_is_full(self):
        [self.stack.push(i) for i in range(5)]
        self.assertTrue(self.stack.is_full())

    def test_returns_topmost_item_on_the_stack_when_pop_is_called(self):
        [self.stack.push(i) for i in range(5)]
        self.assertEquals(self.stack.pop(), 4)

    def test_raises_exception_when_limit_is_exceeded(self):
        with self.assertRaises(Exception):
            [self.stack.push(i) for i in range(10)]
