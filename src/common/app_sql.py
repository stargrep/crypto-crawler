TABLE_BITCOIN_CREATION = """
    CREATE TABLE IF NOT EXISTS bitcoin (
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

