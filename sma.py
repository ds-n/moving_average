# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
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
