from flask import Flask
from threading import Timer

from crypto_crawler.const import BITCOIN_CRAWLING_PERIOD_SEC, COIN_MARKET_CAP_URL, INSERT_CRYPTO_MANY, CRYPTO_DB_NAME, \
    CREATE_TABLE_CRYPTO
from crypto_crawler.strategy import create_crypto_file
from crypto_crawler.web_api_handler import get_web_content
from crypto_crawler.notification import alarm_arbitrage
from crypto_crawler.sql_utils import write_many, write

app = Flask(__name__)
crawl_enabled = True


def crawl_bitcoin_price() -> None:
    print("start crawling!")
    bitcoin_prices = get_web_content()
    # bitcoin_prices = filter_invalid_records(bitcoin_prices)
    write_many(INSERT_CRYPTO_MANY, CRYPTO_DB_NAME, list(map(lambda x: x.to_tuple(), bitcoin_prices)))
    alarm_arbitrage(bitcoin_prices)
    # alarm_prediction()
    if crawl_enabled:
        Timer(BITCOIN_CRAWLING_PERIOD_SEC, crawl_bitcoin_price).start()
    else:
        print("crawl paused!")
        return

    # actual crawl


@app.route("/pause")
def pause() -> str:
    global crawl_enabled
    crawl_enabled = False
    return "PAUSED!"


@app.route("/status")
def status() -> str:
    return "100%"


@app.route("/")
def default():
    return "SAMPLE TRADING SYSTEM"


@app.route("/create-file")
def create_file():
    create_crypto_file(CRYPTO_DB_NAME)
    return "CREATED!"


if __name__ == "__main__":
    write(CREATE_TABLE_CRYPTO, CRYPTO_DB_NAME)
    crawl_bitcoin_price()
    app.run()
