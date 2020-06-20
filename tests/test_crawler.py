import unittest

from crypto_crawler.common import get_system_milli
from crypto_crawler.const import COIN_MARKET_CAP_URL, CRYPTO_DB_NAME, INSERT_CRYPTO_MANY, TEST_DB_NAME
from crypto_crawler.crawler import get_web_content
from crypto_crawler.sql_utils import write, write_many


class TestCrawler(unittest.TestCase):
    crypto_map = {}
    testing_time = get_system_milli()

    # Returns True or False.
    def test_crypto(self):
        self._setup_crypto()
        self._compare_crypto()
        write_many(INSERT_CRYPTO_MANY, TEST_DB_NAME, tuple(map(lambda c: c.to_tuple(), self.crypto_map)))
        # print()

    def _setup_crypto(self):
        self.crypto_map = get_web_content(COIN_MARKET_CAP_URL)

    def _compare_crypto(self):
        # this is NOT a very robust test
        print(self.crypto_map)
        self.assertTrue(len(self.crypto_map) > 0)
