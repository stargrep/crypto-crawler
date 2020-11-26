from crypto_crawler.const import COIN_MARKET_CAP_URL
from crypto_crawler.app import start_app


def main_func():
    print("hello, ", COIN_MARKET_CAP_URL)
    start_app()


main_func()
