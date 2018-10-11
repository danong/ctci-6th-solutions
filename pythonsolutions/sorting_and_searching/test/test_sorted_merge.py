import unittest

from ..sorted_merge import merge


class Test(unittest.TestCase):
    def test_simple(self):
        a = [1, 3, 5, None, None, None]
        b = [2, 4, 6]
        merge(a, b)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6])
