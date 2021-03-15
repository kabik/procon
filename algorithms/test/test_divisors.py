import unittest

from .. import divisors

class TestDivisors(unittest.TestCase):
    def test_empty(self):
        l = divisors.divisors(0)
        self.assertEqual(l, [])

    def test_one(self):
        l = divisors.divisors(1)
        self.assertEqual(l, [1])

    def test_prime(self):
        l = divisors.divisors(97)
        self.assertEqual(l, [1, 97])

    def test_many(self):
        l = divisors.divisors(100)
        self.assertEqual(l, [1,2,4,5,10,20,25,50,100])
