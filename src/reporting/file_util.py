import pandas as pd
from os import path

from src.common.app_constant import CSV_FOLDER_PATH


def write_as_new_file(file_name, data_list, column_list):
    full_path = path.join(CSV_FOLDER_PATH, file_name)
    df = pd.DataFrame(data_list, columns=column_list)
    df.to_csv(full_path, index=False)


def read_as_df(file_name):
    full_path = path.join(CSV_FOLDER_PATH, file_name)
    return pd.read_csv(full_path)




