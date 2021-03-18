import unittest
import time

import gcd

class TestGcd(unittest.TestCase):
    @staticmethod
    def exec(n1, n2):
        start = time.time()
        ans = gcd.gcd(n1, n2)
        end = time.time()
        return ans, end-start

    def test_1_1(self):
        ans, exec_time = self.exec(1,1)
        self.assertEqual(ans, 1)
        self.assertLess(exec_time, 0.001)

    def test_prime(self):
        ans, exec_time = self.exec(11,13)
        self.assertEqual(ans, 1)
        self.assertLess(exec_time, 0.001)

    def test_prime_big(self):
        ans, exec_time = self.exec(2147483647, 6700417)
        self.assertEqual(ans, 1)
        self.assertLess(exec_time, 0.001)

    def test_composite_small(self):
        ans, exec_time = self.exec(36, 24)
        self.assertEqual(ans, 12)
        self.assertLess(exec_time, 0.001)

    def test_composite_big_1(self):
        ans, exec_time = self.exec(2**100, 2)
        self.assertEqual(ans, 2)
        self.assertLess(exec_time, 0.001)

    def test_composite_big_2(self):
        ans, exec_time = self.exec(2**10 * 3**5 * 5**2,  2**5 * 3**10 * 5**4)
        self.assertEqual(ans, 2**5 * 3**5 * 5**2)
        self.assertLess(exec_time, 0.001)
