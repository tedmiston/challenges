"""
Minimal unit tests.
"""

import unittest

from solution import factorize, is_factor, is_prime, lpf


class TestIsFactor(unittest.TestCase):

    def test_5_1(self):
        self.assertTrue(is_factor(5, 1))

    def test_5_2(self):
        self.assertFalse(is_factor(5, 2))

    def test_5_5(self):
        self.assertTrue(is_factor(5, 5))

    def test_12_2(self):
        self.assertTrue(is_factor(12, 2))

    def test_12_3(self):
        self.assertTrue(is_factor(12, 3))

    def test_12_4(self):
        self.assertTrue(is_factor(12, 4))

    def test_12_6(self):
        self.assertTrue(is_factor(12, 6))

    def test_12_7(self):
        self.assertFalse(is_factor(12, 7))


class TestFactorize(unittest.TestCase):

    def test_6(self):
        self.assertEqual(factorize(6), [6, 3, 2, 1])

    def test_10(self):
        self.assertEqual(factorize(10), [10, 5, 2, 1])

    def test_12(self):
        self.assertEqual(factorize(12), [12, 6, 4, 3, 2, 1])


class TestIsPrime(unittest.TestCase):

    def test_1(self):
        self.assertTrue(is_prime(1))

    def test_7(self):
        self.assertTrue(is_prime(7))

    def test_8(self):
        self.assertFalse(is_prime(8))

    def test_1000(self):
        self.assertFalse(is_prime(1000))

    def test_524287(self):
        self.assertTrue(is_prime(524287))


class TestLargestPrimeFactor(unittest.TestCase):

    def test_13195(self):
        self.assertEqual(lpf(13195), 29)

    def test_600851475143(self):
        self.assertEqual(lpf(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
