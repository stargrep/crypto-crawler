import time
import re


def get_system_milli():
    return time.time_ns() // 1000000


def convert_as_number(symbol):
    """
    handle cases:
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


