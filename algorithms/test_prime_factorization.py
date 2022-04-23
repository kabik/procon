import unittest

import prime_factorization

class TestPrimeFactorization(unittest.TestCase):
    def test_1(self):
        d = prime_factorization.prime_factorization(1)
        self.assertEqual(d, {1: 1})

    def test_big(self):
        d = prime_factorization.prime_factorization(150150)
        self.assertEqual(d, {2: 1, 3: 1, 5: 2, 7: 1, 11: 1, 13: 1})
