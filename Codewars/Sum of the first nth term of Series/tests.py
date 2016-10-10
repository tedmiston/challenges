import unittest

from solution import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_n_0(self):
        self.assertEqual(series_sum(0), '0.00')

    def test_n_1(self):
        self.assertEqual(series_sum(1), '1.00')

    def test_n_2(self):
        self.assertEqual(series_sum(2), '1.25')

    def test_n_3(self):
        self.assertEqual(series_sum(3), '1.39')

    def test_n_5(self):
        self.assertEqual(series_sum(5), '1.57')

if __name__ == '__main__':
    unittest.main()
