import unittest
from math import isclose

from crypto_crawler.technical_analysis import get_data_in_range, cal_tr, cal_smooth_constant, \
    append_effect_ratio


class TestReporting(unittest.TestCase):

    def test_get_data_in_range(self):
        assert len(get_data_in_range("600309", "2010/01/02", "2020/01/15")) > 0


    def test_cal_tr(self):
        data = get_data_in_range("600309", "2010/01/02", "2020/01/15")
        print(data.iloc[0])
        print(data.iloc[1])
        print(cal_tr(data.iloc[1], data.iloc[0]))
        assert cal_tr(data.iloc[1], data.iloc[0]) > 0


    def test_smooth_constant(self):
        assert isclose(cal_smooth_constant(1), 2 / 3)
        assert isclose(cal_smooth_constant(0.5), 34 / 93)


    def test_append_effect_ratio(self):
        df = get_data_in_range("600309", "2010/01/02", "2020/01/15")
        print(append_effect_ratio(df))