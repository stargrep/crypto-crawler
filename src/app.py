from flask import Flask
import threading
from src.crawler import get_web_content
from src.common.app_constant import BITCOIN_CRAWLING_PERIOD_SEC, BITCOIN_PRICE_URL, MSG_PREDICTION_NOT_READY
from src.crawler.validate import filter_invalid_records

app = Flask(__name__)
timer = None


def get_bitcoin_price():
    """
    setup global timer
    :return:
    """
    bitcoin_prices = get_web_content(BITCOIN_PRICE_URL)
    print(filter_invalid_records(bitcoin_prices))
    return threading.Timer(BITCOIN_CRAWLING_PERIOD_SEC, get_bitcoin_price)


# TODO: think about how to implement this end point
@app.route("/stop-crawl")
def stop_crawl():
    """
    stop crawling but keep web server running
    :return: string
    """
    timer.cancel()
    return "STOPPED!"


@app.route("/re-crawl")
def activate_job():
    timer = get_bitcoin_price()
    timer.start()
    return "RE-CRAWL"


@app.route("/predict")
def get_next_prediction():
    return MSG_PREDICTION_NOT_READY


@app.route("/health")
def health():
    return "GREEN"


@app.route("/")
def health():
    return "SAMPLE TRADING SYSTEM"


if __name__ == "__main__":
    timer = get_bitcoin_price()
    timer.start()

    app.run()
