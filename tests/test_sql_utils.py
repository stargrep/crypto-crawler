import unittest

from crypto_crawler.common import get_system_milli
from crypto_crawler.const import SELECT_DUMMY, TEST_DB_NAME, CREATE_TABLE_DUMMY, INSERT_MANY_DUMMY, DELETE_DUMMY, \
    DROP_DUMMY, CREATE_TABLE_CRYPTO, SELECT_CRYPTO_RECENT_500, CRYPTO_DB_NAME
from crypto_crawler.sql_utils import execute_read, execute_write, execute_write_many, get_data


class SqlUtilTest(unittest.TestCase):
    test_time = get_system_milli()

    # def test_select_dummy(self):
    #     result = execute_read(SELECT_DUMMY, TEST_DB_NAME)
    #     print(result)
    #     self.assertTrue(result is not None and len(result) > 0)

    def testInsertDummyData(self):
        # get all. insert 3, check, remove, then check
        data_list = [
            ('AKM Semiconductor Inc.', 100000000.0),
            ('Asahi Glass Co Ltd.', 10000000002.0),
            ('Daikin Industries Ltd.', 1000000003.0)
        ]
        execute_write(CREATE_TABLE_DUMMY, TEST_DB_NAME)
        execute_write_many(INSERT_MANY_DUMMY, TEST_DB_NAME, data_list)
        results = get_data(SELECT_DUMMY, TEST_DB_NAME)
        print(results)
        self.assertTrue(len(get_data(SELECT_DUMMY, TEST_DB_NAME)) == 3)

        for result in results:
            execute_write(DELETE_DUMMY, TEST_DB_NAME, result[0])
        self.assertTrue(len(get_data(SELECT_DUMMY, TEST_DB_NAME)) == 0)
        execute_write(DROP_DUMMY, TEST_DB_NAME)

    def testSelectCrypto(self):
        execute_write(CREATE_TABLE_CRYPTO, CRYPTO_DB_NAME)
        result = get_data(SELECT_CRYPTO_RECENT_500, CRYPTO_DB_NAME)
        print(result)
        print("the crypto table size: " + str(len(result)))
        self.assertTrue(result is not None and len(result) >= 0)
