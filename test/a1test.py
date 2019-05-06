import unittest
from a1 import count_words


class TestAssignment1(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(4, count_words("cat dog rat hat"))
        self.assertEqual(4, count_words("ravi pintu vijay prakash"))


if __name__ == '__main__':
    unittest.main()