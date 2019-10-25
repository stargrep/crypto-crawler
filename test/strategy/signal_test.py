import unittest
from src.crawler import get_web_content
from src.common.app_util import get_system_milli
from src.common.app_constant import BITCOIN_PRICE_URL
from src.strategy.signal import arbitrage_signal


class SignalTest(unittest.TestCase):

    crypto_list = []
    price_milli = get_system_milli()

    def setUp(self):
        pass

    # Returns True or False.
    def testCryptoClass(self):
        self.__setupCrypto__()
        self.__compareCrypto__()

    def __setupCrypto__(self):
        self.crypto_list = get_web_content(BITCOIN_PRICE_URL)

    def __compareCrypto__(self):
        # this is NOT a very robust test
        print(self.crypto_list)
        print(arbitrage_signal(self.crypto_list))


if __name__ == '__main__':
    unittest.main()
