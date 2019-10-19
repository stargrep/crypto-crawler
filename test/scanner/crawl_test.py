import unittest
import time
from src.data_model import CryptoPrice


class SimpleTest(unittest.TestCase):

    crypto = None
    expected_crypto_map = None
    price_milli = time.time_ns() // 1000000

    def setUp(self):
        pass

    # Returns True or False.
    def testCryptoClass(self):
        self.__setupCrypto__()
        self.__compareCrypto__()

    def __setupCrypto__(self):
        pass

    def __compareCrypto__(self):
        self.assertTrue(self.crypto.as_dict() == self.expected_crypto_map)


if __name__ == '__main__':
    unittest.main()
