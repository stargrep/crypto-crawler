import unittest

from crypto_crawler.common import get_system_milli
from crypto_crawler.const import COIN_MARKET_CAP_URL
from crypto_crawler.crawler import get_web_content


class SimpleTest(unittest.TestCase):
    crypto_map = {}
    testing_time = get_system_milli()

    def setUp(self):
        pass

    # Returns True or False.
    def testCryptoClass(self):
        self.__setupCrypto__()
        self.__compareCrypto__()

    def __setupCrypto__(self):
        self.crypto_map = get_web_content(COIN_MARKET_CAP_URL)

    def __compareCrypto__(self):
        # this is NOT a very robust test
        print(self.crypto_map)
        self.assertTrue(len(self.crypto_map) > 0)
