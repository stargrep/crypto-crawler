import pandas as pd

from crypto_crawler.reporting import read_as_df


def get_data_in_range(code: str,
                      start_at_str: str,
                      end_at_str: str,
                      look_back_dates: int = 30,
                      file: str = "shangzheng50.csv") -> pd.DataFrame:
    data = read_as_df(file)
    data.dropna(inplace=True)
    code_data = data[data["CODES"].str.startswith(code)]
    if start_at_str is not None:
        code_data = code_data[code_data["DATES"] >= start_at_str]
    if end_at_str is not None:
        code_data = code_data[code_data["DATES"] <= end_at_str]

    return code_data


def cal_tr(curr: pd.Series, prev: pd.Series) -> float:
    tr = max(abs(curr["HIGH"] - curr["LOW"]),
             abs(curr["HIGH"] - prev["CLOSE"]),
             abs(prev["CLOSE"] - curr["LOW"]))
    return tr


def cal_smooth_constant(prev_tr: float, ns: int = 2, nl: int = 30) -> float:
    return prev_tr * (2 / (ns + 1) - 2 / (nl + 1)) + 2 / (nl + 1)


def append_effect_ratio(data: pd.DataFrame) -> pd.DataFrame:
    # Append TR
    for i in range(1, len(data)):
        data.loc[data.index[i], 'TR'] = cal_tr(data.iloc[i], data.iloc[i - 1])

    abs_close = (data['CLOSE'] - data['CLOSE'].shift(periods=7, fill_value=0)).abs()
    abs_tr_sum7 = data['TR'].abs().rolling(7).sum()
    # Append EFFECT_RATIO
    data['EFFECT_RATIO'] = abs_close / abs_tr_sum7

    # Append SMOOTH
    data['SMOOTH'] = data['EFFECT_RATIO'].shift(1).apply(lambda x: cal_smooth_constant(x))

    # Append MIDDLE, FROM AMA
    ama = [data.iloc[0]['CLOSE']]
    prev_ama = ama[0]
    for i in range(1, len(data)):
        cur_ama = prev_ama + data.iloc[i]['SMOOTH'] * (data.iloc[i]['CLOSE'] - prev_ama)
        ama.append(cur_ama)
    data['MIDDLE'] = ama
    data['MIDDLE'] = data['MIDDLE'].shift(3)

    # Append TOP and BOTTOM, from ma3, ma30 and smooth_std7
    smooth_std7 = data['SMOOTH'].rolling(7).std()

    data['TOP'] = data['MIDDLE'] + 16 / 10 * smooth_std7
    data['BOTTOM'] = data['MIDDLE'] - 16 / 10 * smooth_std7

    data['BUY'] = cal_buy(data)
    data['SELL'] = cal_sell(data)
    return data


def cal_buy(data: pd.DataFrame, look_back_dates: int = 30) -> [int]:
    ma5 = data['CLOSE'].rolling(5).mean()
    ma30 = data['CLOSE'].rolling(30).mean()
    buys = []
    for i in range(len(data)):
        if i > look_back_dates:
            yesterday = data.iloc[i - 1]
            middle = yesterday['MIDDLE']
            if check_cross(middle, i, ma5) and \
                    yesterday['CLOSE'] >= ma30.iloc[i - 1] and \
                    yesterday['CLOSE'] >= yesterday['HIGH']:
                # if check_cross(middle, i, ma5):
                buys.append(1)
            else:
                buys.append(0)
        else:
            buys.append(0)
    return buys


def check_cross(middle: float, date: int, ma: pd.Series, size: int = 5) -> bool:
    for count in range(size):
        # from trade date -> it's yesterday 's middle
        # and 5 days before yesterday.
        if middle > ma.iloc[date - count - 2]:
            return False
    return middle >= ma.iloc[date - 1]


def cal_sell(data: pd.DataFrame, look_back_dates: int = 30) -> [int]:
    ma3 = data['CLOSE'].rolling(3).mean()
    sells = []
    for i in range(len(data)):
        if i > look_back_dates:
            yesterday = data.iloc[i - 1]
            if check_long_cross(yesterday['HIGH'], ma3, i) and yesterday['CLOSE'] < yesterday['OPEN']:
                sells.append(1)
            else:
                sells.append(0)
        else:
            sells.append(0)
    return sells


def check_long_cross(high: float,
                     ma: pd.Series,
                     date: int,
                     size: int = 15) -> bool:
    for count in range(size):
        if ma.iloc[date - 2 - count] > high:
            return False
    return ma.iloc[date - 1] >= high


# TR, EFFECT_RATIO, SMOOTH, AMA
# MA3, MA30, SMOOTH_STD7
# TOP, BOTTOM, MIDDLE
# BUY, SELL
# POSITION, ASSET



