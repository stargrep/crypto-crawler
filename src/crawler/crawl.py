import requests
from bs4 import BeautifulSoup

from src.common.app_util import get_system_milli, convert_as_number
from src.data_model import CryptoPrice
from src.common import COIN_NAME_BITCOIN
from src.common import TARGET_EXCHANGE_SET


def map_list_to_price(line):
    """
    expected line:
        ['1', 'BKEX', 'BTC/USDT', '$404,691,250', '$8105.52', '2.81%', 'Spot', 'Percentage', 'Recently']

    :param line: list
    :return: CryptoPrice
    """
    return CryptoPrice(exchange=line[1],
                       coin_name=COIN_NAME_BITCOIN,
                       price=convert_as_number(line[4]),
                       pricing_epoch_milli=get_system_milli(),
                       volume=convert_as_number(line[3]),
                       volume_p=convert_as_number(line[5]) / 100,
                       fee_type=line[7],
                       coin_pair=line[2])


def get_web_content(url, target_exchanges=TARGET_EXCHANGE_SET):
    """
    request for crypto price page and convert to dict of CryptoPrice

    :param url:                 price url to crawl
    :param target_exchanges:    internal map to filter needed information
    :return:                    list<CryptoPrice>
    """

    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    exchange_price = []
    price_table = s.find_all('tbody')[0].contents
    for row in price_table:
        if len(row) > 1:
            line = row.text
            filtered_line = [i for i in line.split("\n") if len(i) > 0]
            # check if the exchange we want
            if filtered_line[1] in target_exchanges:
                exchange_price.append(map_list_to_price(filtered_line))
    return exchange_price

