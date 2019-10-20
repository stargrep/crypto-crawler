from flask import Flask
import threading
from src.crawler import get_web_content
from src.common.app_constant import BITCOIN_CRAWLING_PERIOD_SEC, BITCOIN_PRICE_URL
from src.crawler.validate import filter_invalid_records

app = Flask(__name__)


def get_bitcoin_price():
    bitcoin_prices = get_web_content(BITCOIN_PRICE_URL)
    print(filter_invalid_records(bitcoin_prices))
    threading.Timer(BITCOIN_CRAWLING_PERIOD_SEC, get_bitcoin_price).start()


# TODO: think about how to implement this end point
@app.route("/stop-crawl")
def stop_crawl():
    """
    stop crawling but keep web server running
    :return: string
    """
    return "STOPPED!"


@app.route("/active-jobs")
def active_jobs():
    pass


@app.route("/health")
def health():
    return "GREEN"


if __name__ == "__main__":
    get_bitcoin_price()
    app.run()
