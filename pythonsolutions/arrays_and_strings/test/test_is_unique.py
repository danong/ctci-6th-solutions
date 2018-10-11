import unittest

from ..is_unique import unique_characters, unique_characters_ds


class Test(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('aa', False),
            ('ab', True)
        ]

    def test_unique_characters(self):
        for a, expected_ans in self.test_cases:
            self.assertEqual(unique_characters(a), expected_ans)

    def test_unique_characters_ds(self):
        for a, expected_ans in self.test_cases:
            self.assertEqual(unique_characters_ds(a), expected_ans)
