import unittest
from ..howSum import how_sum, how_sum_memo

class TestHowSum(unittest.TestCase):

    def assertInAnyOrder(self, result, expected):
        self.assertIsNotNone(result)
        self.assertEqual(sorted(result), sorted(expected))

    def test_how_sum(self):
        self.assertInAnyOrder(how_sum(7, [2, 3]), [2, 2, 3])
        self.assertInAnyOrder(how_sum(7, [5, 3, 4, 7]), [4, 3])
        self.assertIsNone(how_sum(7, [2, 4]))
        self.assertInAnyOrder(how_sum(8, [2, 3, 5]), [2, 2, 2, 2])
    
    def test_how_sum_memo(self):
        self.assertInAnyOrder(how_sum_memo(7, [2, 3], {}), [2, 2, 3])
        self.assertInAnyOrder(how_sum_memo(7, [5, 3, 4, 7], {}), [4, 3])
        self.assertIsNone(how_sum_memo(7, [2, 4], {}))
        self.assertInAnyOrder(how_sum_memo(8, [2, 3, 5], {}), [2, 2, 2, 2])
        self.assertIsNone(how_sum_memo(300, [7,14], {}))

if __name__ == "__main__":
    unittest.main()