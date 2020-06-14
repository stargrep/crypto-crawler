import unittest

from crypto_crawler.common import get_system_milli
from crypto_crawler.const import SELECT_DUMMY, TEST_DB_NAME, CREATE_TABLE_DUMMY, INSERT_MANY_DUMMY, DELETE_DUMMY, \
    DROP_DUMMY, CREATE_TABLE_CRYPTO, SELECT_CRYPTO_RECENT_500, CRYPTO_DB_NAME
from crypto_crawler.sql_utils import read, write, write_many


class TestSqlUtils(unittest.TestCase):
    test_time = get_system_milli()

    # def test_select_dummy(self):
    #     result = execute_read(SELECT_DUMMY, TEST_DB_NAME)
    #     print(result)
    #     self.assertTrue(result is not None and len(result) > 0)

    def test_dummy(self):
        # get all. insert 3, check, remove, then check
        data_list = [
            ('AKM Semiconductor Inc.', 100000000.0),
            ('Asahi Glass Co Ltd.', 10000000002.0),
            ('Daikin Industries Ltd.', 1000000003.0)
        ]
        write(CREATE_TABLE_DUMMY, TEST_DB_NAME)
        write_many(INSERT_MANY_DUMMY, TEST_DB_NAME, data_list)
        results = read(SELECT_DUMMY, TEST_DB_NAME)
        print(results)
        self.assertTrue(len(read(SELECT_DUMMY, TEST_DB_NAME)) == 3)

        for result in results:
            write(DELETE_DUMMY, TEST_DB_NAME, result[0])
        self.assertTrue(len(read(SELECT_DUMMY, TEST_DB_NAME)) == 0)
        write(DROP_DUMMY, TEST_DB_NAME)

    def test_read_crypto(self):
        write(CREATE_TABLE_CRYPTO, CRYPTO_DB_NAME)
        result = read(SELECT_CRYPTO_RECENT_500, CRYPTO_DB_NAME)
        print(result)
        print("the crypto table size: " + str(len(result)))
        self.assertTrue(result is not None and len(result) >= 0)
