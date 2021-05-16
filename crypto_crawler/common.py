import time
import re
from datetime import datetime


def milli_to_datetime_str(milli: int) -> str:
    return datetime.fromtimestamp(milli / 1000).strftime('%Y-%m-%d %H:%M:%S')


def get_system_milli() -> int:
    return time.time_ns() // 1000000


def convert_as_number(symbol: str) -> float:
    """
    handle cases:
        '  ' or ''      -> 0
        '10.95%'        -> 10.95
        '$404,691,250'  -> 404691250
        '$8105.52'      -> 8105.52
    :param symbol:      string
    :return:            float
    """
    result = symbol.strip()
    if len(result) == 0:
        return 0

    result = re.sub('[%$, *]', '', result)

    return float(result)


