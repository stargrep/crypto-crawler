COIN_MARKET_CAP_URL = "https://coinmarketcap.com/currencies/bitcoin/markets"

COIN_NAME_BITCOIN = "BitCoin"
COIN_NAME_ETC = "ETC"

TARGET_EXCHANGE_SET = {"Coinbase Pro", "Binance", "Luno", "Gemini", "Bitfinex", "CoinsBank"}
TARGET_COIN_PAIR = {"BTC/USD", "BTC/USDT"}
CRYPTO_SYMBOL_SET = {COIN_NAME_BITCOIN, COIN_NAME_ETC}

TEST_DB_NAME = "test.db"
CRYPTO_DB_NAME = "crypto.db"

BITCOIN_CRAWLING_PERIOD_SEC = 5

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
    FROM crypto_price where exchange = 'Binance'
    ORDER BY id desc LIMIT 500;
"""

INSERT_CRYPTO_MANY = """
    INSERT INTO crypto_price3(exchange, coin_name, price, pricing_time, volume, volume_p, fee_type, coin_pair) 
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
