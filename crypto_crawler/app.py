from flask import Flask
from threading import Timer

from crypto_crawler.const import BITCOIN_CRAWLING_PERIOD_SEC

app = Flask(__name__)
crawl_enabled = True


def crawl_bitcoin_price():
    print("start crawling!")
    if crawl_enabled:
        Timer(BITCOIN_CRAWLING_PERIOD_SEC, crawl_bitcoin_price).start()
    else:
        print("crawl paused!")
        return

    # actual crawl


@app.route("/stop")
def stop():
    global crawl_enabled
    crawl_enabled = False
    return "STOPPED!"


@app.route("/status")
def status():
    return "100%"


@app.route("/")
def default():
    return "SAMPLE TRADING SYSTEM"


if __name__ == "__main__":
    crawl_bitcoin_price()
    app.run()
