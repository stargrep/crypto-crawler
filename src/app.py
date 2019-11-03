from flask import Flask
import threading

from src.crawler import get_web_content
from src.common.app_constant import BITCOIN_CRAWLING_PERIOD_SEC, BITCOIN_PRICE_URL, MSG_PREDICTION_NOT_READY
from src.crawler.validate import filter_invalid_records, alarm_arbitrage
from src.data_storage.pgsql_util import insert_many

app = Flask(__name__)
crawl_enabled = True


def get_bitcoin_price():
    """
    setup global timer
    :return:
    """
    bitcoin_prices = get_web_content(BITCOIN_PRICE_URL)
    bitcoin_prices = filter_invalid_records(bitcoin_prices)
    # insert_many(INSERT_CRYPTO_MANY, list(map(lambda x: x.to_tuple(), bitcoin_prices)))
    # alarm_arbitrage(bitcoin_prices)
    # alarm_prediction()
    if crawl_enabled:
        threading.Timer(BITCOIN_CRAWLING_PERIOD_SEC, get_bitcoin_price).start()
    else:
        return


@app.route("/stop-crawl")
def stop_crawl():
    """
    stop crawling but keep web server running
    :return: string
    """
    global crawl_enabled
    crawl_enabled = False
    return "STOPPED!"


@app.route("/re-crawl")
def activate_job():
    global crawl_enabled
    crawl_enabled = True
    get_bitcoin_price()
    return "RE-CRAWL"


@app.route("/predict")
def get_next_prediction():
    return MSG_PREDICTION_NOT_READY


@app.route("/health")
def health():
    return "GREEN"


@app.route("/")
def default():
    return "SAMPLE TRADING SYSTEM"


if __name__ == "__main__":

    get_bitcoin_price()

    app.run()
