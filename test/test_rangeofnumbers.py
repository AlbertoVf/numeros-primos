from unittest import TestCase

from src.rangeofnumbers import RangeOfNumbers


class TestRangeOfNumbers(TestCase):
    s = 1000000
    f = 2000000

    def test_create_range(self):
        range = RangeOfNumbers(start=self.s)
        self.assertEqual(range.start, self.s)
        self.assertEqual(range.final, 2000000)

    def test_create_range_with_final(self):
        range = RangeOfNumbers(start=self.s, final=self.f)
        self.assertEqual(range.start, 1000000)
        self.assertEqual(range.final, 2000000)

    def test_create_range_empty(self):
        range = RangeOfNumbers()
        self.assertEqual(range.start, 0)
        self.assertEqual(range.final, 1000000)

    def test_file_name(self):
        range = RangeOfNumbers(start=self.s)
        self.assertEqual(range.file, f'{self.s}-{self.f}')
