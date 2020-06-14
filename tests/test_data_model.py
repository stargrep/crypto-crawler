import unittest

from crypto_crawler.data_model import CryptoPrice


class TestDataModel(unittest.TestCase):

    def test_simple(self):
        record = CryptoPrice()
        record.exchange = "Binance"
        record.coin_name = "Bitcoin"
        record.price = 10000.0
        assert record.to_tuple()[1] == "Bitcoin"


if __name__ == '__main__':
    unittest.main()
