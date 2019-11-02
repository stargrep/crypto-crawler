from src.common.app_sql import SELECT_CRYPTO_RECENT_500
from src.data_model import CryptoPrice
from src.data_storage.pgsql_util import get_data
from src.reporting import write_as_new_file


def create_crypto_file():
    """
    train : test = 4 : 1
    400 100 records
    :return:
    """
    crypto_list = get_data(SELECT_CRYPTO_RECENT_500)
    train = crypto_list[:400]
    test = crypto_list[400:]
    write_as_new_file("train.csv", train, CryptoPrice.get_col_list())
    write_as_new_file("test.csv", test, CryptoPrice.get_col_list())


if __name__ == "__main__":
    create_crypto_file()
