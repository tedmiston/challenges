"""
https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series
"""

from decimal import Decimal


def series_sum(n):
    if n == 0:
        sum_ = 0
    else:
        sum_ = 1
        for i in range(n-1):
            nth_value = 1 / (4+3*i)
            sum_ += nth_value

    sum_str = str(round(Decimal(sum_), 2))
    return sum_str
