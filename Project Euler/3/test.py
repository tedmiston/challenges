"""
Minimal unit tests.
"""

from nose2.tools.params import params

from solution import factorize, is_factor, is_prime, lpf


@params(
    (5, 1, True),
    (5, 2, False),
    (5, 5, True),
    (12, 2, True),
    (12, 3, True),
    (12, 4, True),
    (12, 6, True),
    (12, 7, False),
)
def test_is_factor(n, i, expected):
    assert is_factor(n, i) == expected


@params(
    (6, [6, 3, 2, 1]),
    (10, [10, 5, 2, 1]),
    (12, [12, 6, 4, 3, 2, 1]),
)
def test_factorize(n, factors):
    assert factorize(n) == factors


@params(
    (1, True),
    (7, True),
    (8, False),
    (1000, False),
    (524287, True),
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected


@params(
    (13195, 29),
    (600851475143, 6857),
)
def test_largest_prime_factor(n, expected):
    assert lpf(n) == expected
