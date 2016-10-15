from nose2.tools.params import params

from solution import series_sum


@params(
    (0, '0.00'),
    (1, '1.00'),
    (2, '1.25'),
    (3, '1.39'),
    (5, '1.57'),
)
def test_series_sum_n(n, expected):
    assert series_sum(n) == expected
