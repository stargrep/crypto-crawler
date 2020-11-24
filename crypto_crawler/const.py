from pathlib import Path

COIN_MARKET_CAP_URL = "https://coinmarketcap.com/currencies/bitcoin/markets"

WEB_API_EXCHANGE_PRICE_URL = "https://web-api.coinmarketcap.com/v1/exchange/market-pairs/latest?id="

COIN_NAME_BITCOIN = "BitCoin"
COIN_NAME_ETC = "ETC"

TARGET_EXCHANGE_SET = {"Binance", "Gemini", "Bitfinex", "CoinsBank"}
TARGET_EXCHANGE_ID = {270, 107, 151, 656}  # 89 - Coinbase Pro

TARGET_COIN_PAIR = {"BTC/USD", "BTC/USDT"}
CRYPTO_SYMBOL_SET = {COIN_NAME_BITCOIN, COIN_NAME_ETC}

TEST_DB_NAME = "test.db"
CRYPTO_DB_NAME = "crypto.db"

BITCOIN_CRAWLING_PERIOD_SEC = 60

BITCOIN_PRICE_ALARM_MIN = 3000          # $USD
BITCOIN_PRICE_ALARM_MAX = 20000         # $USD
BITCOIN_PRICE_VALIDATE_MAX = 30000      # $USD

TRANS_FEE_PERCENTAGE_AVG = 0.0005        # 0.05%

ROOT_DIR = Path(__file__).resolve().parent
CSV_FOLDER_PATH = ROOT_DIR.joinpath("files/csv")

CREATE_TABLE_CRYPTO = """
    CREATE TABLE IF NOT EXISTS crypto_price (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exchange TEXT NOT NULL,
        coin_name TEXT NOT NULL,
        price REAL NOT NULL,
        pricing_time INTEGER NOT NULL,
        volume REAL NOT NULL,
        volume_p REAL NOT NULL,
        fee_type TEXT NOT NULL,
        coin_pair TEXT NOT NULL
    );
"""

SELECT_CRYPTO = """
    SELECT id, exchange, coin_name, price, pricing_time, volume,
        volume_p, fee_type, coin_pair  
    FROM crypto_price where exchange = 'Binance';
"""

SELECT_CRYPTO_RECENT_500 = """
    SELECT id, exchange, coin_name, price, pricing_time,  
        volume, volume_p, fee_type, coin_pair  
    FROM crypto_price WHERE exchange = 'Binance'
    ORDER BY id DESC LIMIT 500;
"""

INSERT_CRYPTO_MANY = """
    INSERT INTO crypto_price(exchange, coin_name, price, pricing_time, volume, volume_p, fee_type, coin_pair) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?)
"""

CREATE_TABLE_DUMMY = """
    CREATE TABLE IF NOT EXISTS dummy (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        update_time REAL NOT NULL
    );
"""

INSERT_MANY_DUMMY = """
    INSERT INTO dummy(content, update_time) VALUES(?, ?);
"""

SELECT_DUMMY = """
    SELECT * FROM dummy;
"""

DELETE_DUMMY = """
    DELETE FROM dummy WHERE id = ?;
"""

DROP_DUMMY = """
    DROP TABLE dummy;
"""
