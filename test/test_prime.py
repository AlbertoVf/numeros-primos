from unittest import TestCase

from src.prime import is_prime, prime_list


class Test(TestCase):
    def test_is_prime(self):
        actual_primes = [2, 3, 5, 7, 11, 97]
        actual_not_primes = [6, 8, 15, 98]

        for i in actual_primes:
            self.assertTrue(is_prime(i))

        for i in actual_not_primes:
            self.assertFalse(is_prime(i))

    def test_special_numbers(self):
        numbers = [0, 1]
        for i in numbers:
            self.assertFalse(is_prime(i))

    def test_prime_list(self):
        actual = prime_list(1, 10)
        expected = [2, 3, 5, 7]
        self.assertEqual(expected, actual)
