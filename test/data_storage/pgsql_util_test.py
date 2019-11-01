import unittest

from src.common import SELECT_PUBLIC
from src.common.app_sql import CREATE_TABLE_DUMMY, INSERT_MANY_DUMMY, SELECT_DUMMY, DELETE_DUMMY, \
    CREATE_TABLE_CRYPTO, SELECT_CRYPTO
from src.common.app_util import get_system_milli
from src.data_storage.pgsql_util import get_data, execute_write, execute_write_many


class SqlUtilTest(unittest.TestCase):
    price_milli = get_system_milli()

    def setUp(self):
        pass

    def testSelectPublic(self):
        result = get_data(SELECT_PUBLIC)
        print(result)
        self.assertTrue(result is not None and len(result) > 0)

    def testInsertDummyData(self):
        # get all. insert 5, check, remove, then check
        data_list = [
            ('AKM Semiconductor Inc.', 100000000),
            ('Asahi Glass Co Ltd.', 10000000002),
            ('Daikin Industries Ltd.', 1000000003)
        ]
        execute_write(CREATE_TABLE_DUMMY)
        execute_write_many(INSERT_MANY_DUMMY, data_list)
        results = get_data(SELECT_DUMMY)
        print(results)
        for result in results:
            execute_write(DELETE_DUMMY, result[0])
        self.assertTrue(len(get_data(SELECT_DUMMY)) == 0)

    def testSelectCrypto(self):
        execute_write(CREATE_TABLE_CRYPTO)
        result = get_data(SELECT_CRYPTO)
        print(result)
        self.assertTrue(result is not None and len(result) >= 0)


if __name__ == '__main__':
    unittest.main()
