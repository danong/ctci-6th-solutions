import unittest

from ..number_swapper import swapper


class Test(unittest.TestCase):
    def test(self):
        a = 123
        b = 345
        a, b = swapper(a, b)
        self.assertEqual(a, 345)
        self.assertEqual(b, 123)
