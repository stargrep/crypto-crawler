from datetime import datetime

COIN_NAME_BITCOIN = "BitCoin"
COIN_NAME_ETC = "ETC"

TARGET_EXCHANGE_SET = {"Coinbase Pro", "Binance", "Luno", "Gemini", "Bitfinex", "CoinsBank"}
TARGET_COIN_PAIR = {"BTC/USD", "BTC/USDT"}
CRYPTO_SYMBOL_SET = {COIN_NAME_BITCOIN, COIN_NAME_ETC}

BITCOIN_PRICE_ALARM_MIN = 3000          # $USD
BITCOIN_PRICE_ALARM_MAX = 20000         # $USD
BITCOIN_PRICE_VALIDATE_MAX = 30000      # $USD

SYSTEM_DATETIME_MIN = datetime(2000, 1, 1)
SYSTEM_DATETIME_MAX = datetime(2099, 12, 31)
SYSTEM_TIME_MIN_MILLI = SYSTEM_DATETIME_MIN.timestamp() * 1000
SYSTEM_TIME_MAX_MILLI = SYSTEM_DATETIME_MAX.timestamp() * 1000

BITCOIN_CRAWLING_PERIOD_SEC = 5        # second

BITCOIN_PRICE_URL = "https://coinmarketcap.com/currencies/bitcoin/#markets"

TRANS_FEE_MIN = 5                       # USD
TRANS_FEE_PERCENTAGE_AVG = 0.002        # 0.2%

PROFIT_PERCENTAGE_MIN = 0.03            # 3%

MSG_PREDICTION_NOT_READY = "Currently prediction strategy is not ready yet!"

