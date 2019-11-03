from src.common.app_constant import TRANS_FEE_PERCENTAGE_AVG


# https://www.investopedia.com/terms/t/trade-signal.asp
def arbitrage_signal(prices):
    """
    apply second best arbitrage with ok profit

    :param prices:
    :return:
    """
    prices.sort(key=lambda price: price.price)
    buy = prices[1]
    sell = prices[-2]
    avg_profit_p = (sell.price * (1 - TRANS_FEE_PERCENTAGE_AVG) -
                    buy.price * (1 + TRANS_FEE_PERCENTAGE_AVG)) / 2 / sell.price * 100
    return {
        "profit": avg_profit_p,
        "buy": buy,
        "sell": sell
    }

