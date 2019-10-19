from src.common import TARGET_EXCHANGE_SET
from src.common.app_constant import CRYPTO_SYMBOL_SET, BITCOIN_PRICE_VALIDATE_MAX, SYSTEM_TIME_MAX_MILLI, \
    SYSTEM_TIME_MIN_MILLI
from src.data_model import CryptoPrice


def validate_price_record(price):
    """
    validation module for crypto price

    :param price: CryptoPrice
    :return: bool
    """
    if type(price) is not CryptoPrice:
        raise Exception("input should be a crypto price object while it's " + price)

    return price.validate() and \
           price.exchange in TARGET_EXCHANGE_SET and \
           price.coin_name in CRYPTO_SYMBOL_SET and \
           (0 < price.price < BITCOIN_PRICE_VALIDATE_MAX) and \
           (SYSTEM_TIME_MIN_MILLI < price.pricing_epoch_milli < SYSTEM_TIME_MAX_MILLI) and \
           price.volume > 0


def alarm_price_range(price):
    """


    :param price: CryptoPrice
    :return: bool
    """

