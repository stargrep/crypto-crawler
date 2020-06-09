import unittest

from crypto_crawler.sample import custom_split


class TestProblem(unittest.TestCase):
    def test_sample(self):
        assert custom_split("1,2,3") == ["1", "2", "3"]


if __name__ == '__main__':
    unittest.main()
