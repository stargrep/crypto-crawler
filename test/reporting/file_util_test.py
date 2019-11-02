import unittest
from src.common.app_util import get_system_milli
from src.crawler import get_web_content
from src.common.app_constant import BITCOIN_PRICE_URL
from src.reporting import write_as_new_file


class SimpleTest(unittest.TestCase):

    price_milli = get_system_milli()

    def setUp(self):
        pass

    def testWriteFile(self):
        # this is NOT a very robust test
        write_as_new_file("test.csv", [["n1", 1], ["n2", 100]], ["col1", "col2"])
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()