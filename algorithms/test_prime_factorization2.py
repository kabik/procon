import unittest

import prime_factorization2

class TestPrimeFactorization2(unittest.TestCase):
    def test_1(self):
        n = 1
        spf = prime_factorization2.smallest_prime_factors(n)
        d = prime_factorization2.prime_factorization(n, spf)
        self.assertEqual(d, {1: 1})

    def test_big(self):
        n = 150150
        spf = prime_factorization2.smallest_prime_factors(n)
        d = prime_factorization2.prime_factorization(n, spf)
        self.assertEqual(d, {2: 1, 3: 1, 5: 2, 7: 1, 11: 1, 13: 1})
