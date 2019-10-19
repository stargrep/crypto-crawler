from src.common import TARGET_EXCHANGE_SET
from src.common.app_constant import CRYPTO_SYMBOL_SET, BITCOIN_PRICE_VALIDATE_MAX, SYSTEM_TIME_MAX_MILLI, \
    SYSTEM_TIME_MIN_MILLI
from src.data_model import CryptoPrice


def validate_price_record(crypto):
    """
    validation module for crypto price

    :param crypto: CryptoPrice
    :return: bool
    """
    if type(crypto) is not CryptoPrice:
        raise Exception("input should be a crypto price object while it's " + crypto)

    return crypto.exchange in TARGET_EXCHANGE_SET and \
        crypto.coin_name in CRYPTO_SYMBOL_SET and \
        (0 < crypto.price < BITCOIN_PRICE_VALIDATE_MAX) and \
        (SYSTEM_TIME_MIN_MILLI < crypto.pricing_epoch_milli < SYSTEM_TIME_MAX_MILLI) and \
        crypto.volume > 0


def filter_invalid_records(crypto_list):
    return [c for c in crypto_list if validate_price_record(c)]


def alarm_price_range(price):
    """
    TODO: check if trigger alarm under some conditions.

    :param price: CryptoPrice
    :return: bool
    """
    return False
