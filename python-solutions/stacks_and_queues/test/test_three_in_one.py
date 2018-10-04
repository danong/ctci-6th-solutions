import unittest

from ..three_in_one import MultiStack


class Test(unittest.TestCase):
    def test_basic(self):
        a = MultiStack(3)
        a.push(1, 0)
        self.assertEqual(a.peek(0), 1)
        a.push(2, 0)
        a.push('apple', 1)
        a.push(3, 0)
        a.push('+', 2)
        a.push('banana', 1)
        self.assertEqual(a.peek(0), 3)
        self.assertEqual(a.pop(0), 3)
        self.assertEqual(a.peek(0), 2)
        a.push('carrot', 1)
        self.assertEqual(a.peek(1), 'carrot')
        self.assertEqual(a.peek(2), '+')
        self.assertEqual(a.pop(0), 2)
        self.assertEqual(a.pop(0), 1)
        self.assertRaises(IndexError, a.pop, 0)
