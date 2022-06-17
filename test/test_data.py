from unittest import TestCase

from src.data import Data


class TestData(TestCase):
    def test_update(self):
        data = Data()
        self.assertEqual("0;0;0.0", str(data))
        data.update("1", 1, 1.0)
        self.assertEqual("1;1;1.0", data.__str__())

    def test_update_as_dict(self):
        data = Data()
        data.__dict__.update({"range": "1", "number_of_primes": 1, "duration": 1.0})
        self.assertEqual("1;1;1.0", data.__str__())
