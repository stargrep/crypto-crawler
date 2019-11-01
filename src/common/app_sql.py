CREATE_TABLE_CRYPTO = """
    CREATE TABLE IF NOT EXISTS crypto_price1 (
        id BIGSERIAL PRIMARY KEY,
        exchange VARCHAR(63) NOT NULL,
        coin_name VARCHAR(31) NOT NULL,
        price DECIMAL NOT NULL,
        pricing_epoch_milli BIGINT NOT NULL,
        volume INT NOT NULL,
        volumn_p DECIMAL NOT NULL,
        fee_type VARCHAR(31) NOT NULL,
        coin_pair VARCHAR(31) NOT NULL
    )
"""

SELECT_CRYPTO = """
    SELECT * FROM crypto_price1
"""

INSERT_CRYPTO_MANY = """
    INSERT INTO crypto_price1(exchange, coin_name, price, pricing_epoch_milli, volume, volume_p, fee_type, coin_pair) 
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
        updated_mili BIGINT NOT NULL
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
