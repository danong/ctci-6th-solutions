import unittest

from ..the_heavy_pill import bottle_id


class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(bottle_id(211.3), 13)
