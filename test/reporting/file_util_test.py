import unittest
from src.common.app_util import get_system_milli
from src.reporting import write_as_new_file
from src.reporting.file_util import read_as_df


class SimpleTest(unittest.TestCase):

    price_milli = get_system_milli()

    def setUp(self):
        pass

    def testWriteFile(self):
        unit_test_file = "unit_test.csv"
        write_as_new_file(unit_test_file, [["n1", 1], ["n2", 100]], ["col1", "col2"])
        self.assertTrue(len(read_as_df(unit_test_file)) > 0)


if __name__ == '__main__':
    unittest.main()
