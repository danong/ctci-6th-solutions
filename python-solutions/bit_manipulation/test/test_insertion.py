import unittest

from ..insertion import insert_bits


class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(insert_bits(0b10000000000, 0b10011, 2, 6),
                         0b10001001100)
        self.assertEqual(insert_bits(0b10110110010, 0b11111, 2, 6),
                         0b10111111110)
