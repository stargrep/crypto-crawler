from os import path

from flask import Flask, send_from_directory, request

from crypto_crawler.const import BITCOIN_CRAWLING_PERIOD_SEC, COIN_MARKET_CAP_URL, INSERT_CRYPTO_MANY, CRYPTO_DB_NAME, \
    CREATE_TABLE_CRYPTO, CSV_FOLDER_PATH
from crypto_crawler.reporting import write_as_new_file
from crypto_crawler.strategy import create_crypto_file
from crypto_crawler.technical_analysis import get_data_in_range, append_effect_ratio
# from crypto_crawler.web_api_handler import get_web_content
from crypto_crawler.notification import alarm_arbitrage
from crypto_crawler.sql_utils import write_many, write

app = Flask(__name__)
crawl_enabled = True


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


@app.route("/create-file")
def create_file():
    create_crypto_file(CRYPTO_DB_NAME)
    return "CREATED!"


@app.route("/query/<code>")
def calculate_range(code):
    start_date = request.args.get('start')
    end_date = request.args.get('end')
    data = append_effect_ratio(get_data_in_range(code, start_date, end_date))
    full_path = path.join(CSV_FOLDER_PATH, "result.csv")
    data.to_csv(full_path, index=False)
    return send_from_directory(CSV_FOLDER_PATH, "result.csv", as_attachment=True)


if __name__ == "__main__":
    app.run()
