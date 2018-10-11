import unittest

from .. import intersection


class Test(unittest.TestCase):
    def test(self):
        a = intersection.LineSegment(intersection.Point(0.0, 0.0),
                                     intersection.Point(1.0, 1.0))
        b = intersection.LineSegment(intersection.Point(1.0, 0.0),
                                     intersection.Point(0.0, 1.0))
        self.assertEqual(intersection.intersection(a, b),
                         intersection.Point(0.5, 0.5))
