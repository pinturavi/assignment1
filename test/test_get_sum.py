from unittest import TestCase
from hof0 import get_sum


class TestGetSum(TestCase):
    def test_get_sum(self):
        self.assertEqual(9, get_sum([2, 3, 4]))
        self.assertEqual(6, get_sum([2, 3, 4], lambda e: e % 2 == 0))
