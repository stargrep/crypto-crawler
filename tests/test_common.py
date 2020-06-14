import unittest

from crypto_crawler.common import convert_as_number


class SimpleTest(unittest.TestCase):

    def test_convert(self):
        print(self)
        assert 10.9 == convert_as_number("10.9")
        assert 1000.0 == convert_as_number("$1,000.00")
        assert 0.0 == convert_as_number("     ")
