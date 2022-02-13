import unittest
import math
from mma import sma, sma_v2


class TestSimpleMovingAverage(unittest.TestCase):

    def test_sma(self):
        res_v1 = sma([1, 2, 3, 7, 9])
        self.assertEqual(res_v1, [math.nan, math.nan, 2.0, 4.0, 6.333333333333333])

    def test_sma_v2(self):
        res_v2 = sma_v2([1, 2, 3, 7, 9])
        self.assertEqual(res_v2, [math.nan, math.nan, 2.0, 4.0, 6.333333333333334])


if __name__ == '__main__':
    unittest.main()
