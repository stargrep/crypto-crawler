from flask import Flask
from threading import Timer

from crypto_crawler.const import BITCOIN_CRAWLING_PERIOD_SEC, COIN_MARKET_CAP_URL
from crypto_crawler.crawler import get_web_content, filter_invalid_records

app = Flask(__name__)
crawl_enabled = True


def crawl_bitcoin_price():
    print("start crawling!")
    bitcoin_prices = get_web_content(COIN_MARKET_CAP_URL)
    bitcoin_prices = filter_invalid_records(bitcoin_prices)
    # write_many(INSERT_CRYPTO_MANY, list(map(lambda x: x.to_tuple(), bitcoin_prices)))
    # alarm_arbitrage(bitcoin_prices)
    # alarm_prediction()
    if crawl_enabled:
        Timer(BITCOIN_CRAWLING_PERIOD_SEC, crawl_bitcoin_price).start()
    else:
        print("crawl paused!")
        return

    # actual crawl


@app.route("/pause")
def pause():
    global crawl_enabled
    crawl_enabled = False
    return "PAUSED!"


@app.route("/status")
def status():
    return "100%"


@app.route("/")
def default():
    return "SAMPLE TRADING SYSTEM"


if __name__ == "__main__":
    crawl_bitcoin_price()
    app.run()
