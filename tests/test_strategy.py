import unittest

from crypto_crawler.const import COIN_MARKET_CAP_URL, TEST_DB_NAME
from crypto_crawler.web_api_handler import get_web_content
from crypto_crawler.strategy import arbitrage_signal, create_crypto_file, arima, arima_validation, earning_calculation


class TestStrategy(unittest.TestCase):


    def test_arbitrage(self):
        crypto_list = get_web_content()
        print(arbitrage_signal(crypto_list))


    def test_create_train(self):
        pass
        # create_crypto_file(TEST_DB_NAME)
        # self.assertTrue(True)

    # Returns True or False.
    def test_predict_ARIMA(self):
        arima()
        self.assertTrue(True)

    def test_Arima_validation(self):
        pred = arima()
        score = arima_validation(pred)
        print(score)
        self.assertTrue(True)

    def test_earning_calculation(self):
        pred = arima()
        earning1 = earning_calculation(arima(), 0.0007)    # 0.07% maker
        earning2 = earning_calculation(arima(), 0.001)    # 0.2% taker
        print(earning1, earning2)
        self.assertTrue(earning1 > 1000)
        self.assertTrue(earning2 <= 0)
