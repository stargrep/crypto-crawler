import requests
from bs4 import BeautifulSoup
import time
import re
from src.data_model import CryptoPrice
from src.main import COIN_NAME_BITCOIN
from src.main import TARGET_EXCHANGE_MAP


# def convert_volume(volume_str):
#     """
#     '$404,691,250' -> '404691250'
#     :param volume_str: string
#     :return: string
#     """
#     return volume_str.replace(",", "").replace("$", "")
#
#
# def convert_money_float(symbol):
#     """
#     '$8105.52' -> 8105.52
#     :param symbol: string
#     :return: float
#     """
#     if "$" in symbol:
#
#     return float(symbol.replace("$", ""))
#
#
# def convert_percentage(p_str):
#     """
#     handle 10.95% or .70%
#     :param p_str: string
#     :return: float
#     """
#     return float(p_str.replace("%", ""))

def convert_as_number(symbol):
    """
    handle case:
        '10.95%' -> 10.95
        '$404,691,250' -> 404691250
        '$8105.52' -> 8105.52

    :param symbol:
    :return:
    """
    result = symbol.strip()
    if len(result) == 0:
        return 0

    result = re.sub('[%$,]', '', result)

    return float(result)


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
                       pricing_epoch_milli=time.time_ns() // 1000000,
                       volume=convert_as_number(line[3]),
                       volume_p=convert_as_number(line[5]) / 100,
                       fee_type=line[7],
                       coin_pair=line[2])


def get_web_content(page, url, target_exchanges=TARGET_EXCHANGE_MAP):
    if page <= 0:
        raise Exception("there is no web content for url: "+ url)
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")

    exchange_price = {}
    price_table = s.find_all('tbody')[0].contents
    for row in price_table:
        if len(row) > 1:
            line = row.text
            filtered_line = [i for i in line.split("\n") if len(i) > 0]
            # check if the exchange we want
            if filtered_line[1] in target_exchanges:
                exchange_price[filtered_line[0]] = map_list_to_price(filtered_line)
    print(exchange_price)


get_web_content(1, "https://coinmarketcap.com/currencies/bitcoin/#markets")
