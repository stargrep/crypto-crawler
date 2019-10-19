from flask import Flask
import threading
from src.crawler import get_web_content
from src.common.app_constant import BITCOIN_CRAWLING_PERIOD_SEC, BITCOIN_PRICE_URL

app = Flask(__name__)


def get_bitcoin_price():
    print("hello, world!!!!")
    print(get_web_content(BITCOIN_PRICE_URL))
    threading.Timer(BITCOIN_CRAWLING_PERIOD_SEC, get_bitcoin_price).start()


@app.route("/")
def health():
    return "GREEN"


if __name__ == "__main__":
    get_bitcoin_price()
    app.run()
