from flask import Flask
import logging
import threading
import time
import requests
from src.crawler import get_web_content
from src.common.app_constant import COIN_NAME_BITCOIN

app = Flask(__name__)


def hello1():
    logging.info("hello, world!!!!")
    get_web_content(1, "https://coinmarketcap.com/currencies/bitcoin/#markets")
    print("test!!!")
    print(COIN_NAME_BITCOIN)
    # threading.Timer(3, hello1).start()


# @app.before_first_request
# def activate_job():
#     def run_job():
#         while True:
#             print("Run recurring task")
#             time.sleep(3)
#
#     thread = threading.Thread(target=run_job)
#     thread.start()


@app.route("/")
def hello():
    return "Hello World!"


def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()


hello1()

if __name__ == "__main__":
    start_runner()
    app.run(debug=True)
