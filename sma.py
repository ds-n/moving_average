# The MIT License (MIT)
#
# Copyright (c) 2015 nicolads87
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================
"""Functions for calculate Simple moving average
https://en.wikipedia.org/wiki/Moving_average
"""

import math


def sma(vec, k=3):
    # window size
    # Initialize an empty list to store moving averages
    moving_averages = []

    for _ in range(k - 1):
        moving_averages.append(math.nan)

    # n is current position in data points
    n = k

    while n <= len(vec):
        sma = sum(vec[n - k:n]) / k
        moving_averages.append(sma)
        n = n + 1

    return moving_averages


def sma_v2(vec, k=3):
    smak = []

    for _ in range(k - 1):
        smak.append(math.nan)

    n = k - 1
    while n < len(vec):
        if math.isnan(smak[len(smak) - 1]):
            sma = sum(vec[n + 1 - k:n + 1]) / k
        else:
            prev = smak[len(smak) - 1]
            sma = prev + ((vec[n] - vec[n - k]) / k)
        smak.append(sma)
        n = n + 1

    return smak


# test

res_v1 = sma([1, 2, 3, 7, 9])
assert res_v1 == [math.nan, math.nan, 2.0, 4.0, 6.333333333333333]

res_v2 = sma_v2([1, 2, 3, 7, 9])
assert res_v2 == [math.nan, math.nan, 2.0, 4.0, 6.333333333333334]
