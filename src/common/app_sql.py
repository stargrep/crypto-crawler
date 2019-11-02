CREATE_TABLE_CRYPTO = """
    CREATE TABLE IF NOT EXISTS crypto_price3 (
        id BIGSERIAL PRIMARY KEY,
        exchange VARCHAR(63) NOT NULL,
        coin_name VARCHAR(31) NOT NULL,
        price DECIMAL NOT NULL,
        pricing_epoch_milli BIGINT NOT NULL,
        volume DECIMAL NOT NULL,
        volume_p DECIMAL NOT NULL,
        fee_type VARCHAR(31) NOT NULL,
        coin_pair VARCHAR(31) NOT NULL
    )
"""

SELECT_CRYPTO = """
    SELECT id, exchange, coin_name, price, pricing_epoch_milli, volume,
        volume_p, fee_type, coin_pair  
    FROM crypto_price3 where exchange = 'Binance'
"""

SELECT_CRYPTO_RECENT_500 = """
    SELECT id, exchange, coin_name, price, 
        to_char(to_timestamp(pricing_epoch_milli/1000), 'YYYY-MM-DD HH24:MI:SS'),
        pricing_epoch_milli,  
        volume, volume_p, fee_type, coin_pair  
    FROM crypto_price3 where exchange = 'Binance'
    ORDER BY id desc LIMIT 500;
"""

INSERT_CRYPTO_MANY = """
    INSERT INTO crypto_price3(exchange, coin_name, price, pricing_epoch_milli, volume, volume_p, fee_type, coin_pair) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
"""

SELECT_PUBLIC = """
SELECT table_schema, table_name FROM information_schema.tables
WHERE table_schema = 'public'
"""

CREATE_TABLE_DUMMY = """
    CREATE TABLE IF NOT EXISTS dummy (
        id SERIAL PRIMARY KEY,
        content VARCHAR(63) NOT NULL,
        updated_mili DECIMAL NOT NULL
    )
"""

INSERT_MANY_DUMMY = """
    INSERT INTO dummy(content, updated_mili) VALUES(%s, %s)
"""

SELECT_DUMMY = """
    SELECT * FROM dummy
"""

DELETE_DUMMY = """
    DELETE FROM dummy WHERE id = %s
"""

DROP_DUMMY = """
    DROP TABLE dummy
"""
