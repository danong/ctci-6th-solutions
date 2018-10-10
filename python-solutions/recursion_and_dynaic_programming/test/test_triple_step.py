import unittest

from ..triple_step import recursive, top_down, bottom_up, pythonic


class Test(unittest.TestCase):
    def setUp(self):
        self.ans = {1: 1, 2: 2, 3: 4, 4: 7, 5: 13, 6: 24, 7: 44, 8: 81, 9: 149,
                    10: 274}

    def test_recursive(self):
        for i in range(1, 11):
            self.assertEqual(recursive(i), self.ans[i])

    def test_top_down(self):
        for i in range(1, 11):
            self.assertEqual(top_down(i), self.ans[i])

    def test_bottom_up(self):
        for i in range(1, 11):
            self.assertEqual(bottom_up(i), self.ans[i])

    def test_pythonic(self):
        for i in range(1, 11):
            self.assertEqual(pythonic(i), self.ans[i])
