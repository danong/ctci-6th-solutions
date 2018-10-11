import unittest

from ..check_permutation import is_permutation


class Test(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ('abc', 'ABC', False),
            ('abc', 'bca', True),
            ('taco cat', 'tac coat', True),
            ('DOG', 'god', False),
            ('abba', 'baba', True),
            ('abba', 'bab', False)
        ]

    def test_is_permutation(self):
        for a, b, expected_ans in self.test_cases:
            self.assertEqual(is_permutation(a, b), expected_ans)
