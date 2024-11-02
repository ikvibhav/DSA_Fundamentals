import unittest
from ..bestSum import best_sum, best_sum_memo

class TestHowSum(unittest.TestCase):

    def assertInAnyOrder(self, result, expected):
        self.assertIsNotNone(result)
        self.assertEqual(sorted(result), sorted(expected))

    def test_best_sum(self):
        self.assertInAnyOrder(best_sum(7, [2, 3]), [2, 2, 3])
        self.assertInAnyOrder(best_sum(7, [5, 3, 4, 7]), [7])
        self.assertIsNone(best_sum(7, [2, 4]))
        self.assertInAnyOrder(best_sum(8, [2, 3, 5]), [3, 5])

    def test_best_sum_memo(self):
        self.assertInAnyOrder(best_sum_memo(7, [2, 3], {}), [2, 2, 3])
        self.assertInAnyOrder(best_sum_memo(7, [5, 3, 4, 7], {}), [7])
        self.assertIsNone(best_sum_memo(7, [2, 4], {}))
        self.assertInAnyOrder(best_sum_memo(50, [1, 2, 25], {}), [25, 25])

if __name__ == "__main__":
    unittest.main()