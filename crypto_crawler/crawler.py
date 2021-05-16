import requests
from bs4 import BeautifulSoup

from crypto_crawler.common import convert_as_number, get_system_milli, milli_to_datetime_str
from crypto_crawler.const import TARGET_EXCHANGE_SET, TARGET_COIN_PAIR, COIN_NAME_BITCOIN, CRYPTO_SYMBOL_SET, \
    BITCOIN_PRICE_VALIDATE_MAX
from crypto_crawler.data_model import CryptoPrice


def map_list_to_price(line: []) -> CryptoPrice:
    """
    expected line:
        ['1', 'BKEX', 'BTC/USDT', '$404,691,250', '$8105.52', '2.81%', 'Spot', 'Percentage', 'Recently']
    :param line: list
    :return: CryptoPrice
    """
    current_time = get_system_milli()
    return CryptoPrice(exchange=line[1],
                       coin_name=COIN_NAME_BITCOIN,
                       price=convert_as_number(line[3]),
                       pricing_time_str=milli_to_datetime_str(current_time),
                       pricing_time=current_time,
                       volume=convert_as_number(line[4]),
                       volume_p=convert_as_number(line[6]) / 100,
                       fee_type=line[8],
                       coin_pair=line[2])


def filter_coin_row(line: [], target_pairs: {str}) -> bool:
    return line[2] in target_pairs


def get_web_content(url: str, target_pairs: {str} = TARGET_COIN_PAIR) -> [CryptoPrice]:
    """
    request for crypto price page and convert to dict of CryptoPrice
    """
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    exchange_price = []
    price_table = s.find_all('tbody')[0].contents
    for row in price_table:
        if len(row) > 1:
            line = row.contents
            filtered_line = [i.text for i in line]
            # check if the exchange we want
            if filter_coin_row(filtered_line, target_pairs):
                try:
                    exchange_price.append(map_list_to_price(filtered_line))
                except Exception as e:
                    print(e)
    return exchange_price


def validate_price_record(crypto: CryptoPrice) -> bool:
    """
    validation module for crypto price
    """
    if type(crypto) is not CryptoPrice:
        raise Exception("input should be a crypto price object while it's " + crypto)

    return crypto.exchange in TARGET_EXCHANGE_SET and \
           crypto.coin_name in CRYPTO_SYMBOL_SET and \
           (0 < crypto.price < BITCOIN_PRICE_VALIDATE_MAX) and \
           crypto.volume > 0


def filter_invalid_records(crypto_list: [CryptoPrice]) -> [CryptoPrice]:
    return [c for c in crypto_list if validate_price_record(c)]
