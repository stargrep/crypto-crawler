import unittest

from crypto_crawler.reporting import write_as_new_file, read_as_df


class TestReporting(unittest.TestCase):

    def test_write_file(self):
        unit_test_file = "unit_test.csv"
        write_as_new_file(unit_test_file, [["n1", 1], ["n2", 100]], ["col1", "col2"])
        self.assertTrue(len(read_as_df(unit_test_file)) > 0)
