import unittest
import math
from mma import wma


class TestWeightedMovingAverage(unittest.TestCase):

    def test_wma(self):
        res_v1 = wma([1, 2, 3, 7, 9])
        self.assertEqual(res_v1, [math.nan, math.nan, 1.0, 1.0, 1.0555555555555556])


if __name__ == '__main__':
    unittest.main()
