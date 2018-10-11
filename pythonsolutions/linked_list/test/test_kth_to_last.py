import random
import unittest

from ..kth_to_last import kth_to_last
from ..linked_list import Node


class Test(unittest.TestCase):
    def setUp(self):
        self.test_cases = []
        for _ in range(10):
            # generate random linked list
            temp_list = random.sample(range(100), random.randint(1, 10))
            head = Node(temp_list[0])
            for val in temp_list[1:]:
                head.append(val)
            # save list, k, and answer
            k = random.randint(1, 10)
            try:
                ans = temp_list[-k]
            except IndexError:
                ans = None
            self.test_cases.append((k, head, ans))

    def test_kth_to_last(self):
        for k, head, expected_ans in self.test_cases:
            try:
                real_ans = kth_to_last(k, head).val
            except AttributeError:
                real_ans = kth_to_last(k, head)
            self.assertEqual(real_ans, expected_ans)
