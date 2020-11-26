import unittest

from crypto_crawler.web_api_handler import query_price, get_web_content


class SimpleTest(unittest.TestCase):


    def test_query_price(self):
        assert query_price(str(270)).price > 0


    def test_get_web_content(self):
        results = get_web_content()
        assert len(results) > 2


