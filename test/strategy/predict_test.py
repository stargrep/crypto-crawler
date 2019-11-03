import unittest
from src.common.app_util import get_system_milli
from src.strategy.predict import arima, create_crypto_file, arima_validation


class SignalTest(unittest.TestCase):
    crypto_list = []
    price_milli = get_system_milli()

    def setUp(self):
        pass

    def testCreateTrainTest(self):
        create_crypto_file()
        self.assertTrue(True)

    # Returns True or False.
    def testPredictARIMA(self):
        arima()
        self.assertTrue(True)

    def testArimaValidation(self):
        pred = arima()
        arima_validation(pred)


if __name__ == '__main__':
    unittest.main()
