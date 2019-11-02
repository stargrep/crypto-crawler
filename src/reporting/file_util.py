import pandas as pd
from os import path

from src.common.app_constant import CSV_FOLDER_PATH


def write_as_new_file(file_name, data_list, column_list):
    total_path = path.join(CSV_FOLDER_PATH, file_name)
    df = pd.DataFrame(data_list, columns=column_list)
    df.to_csv(total_path, index=False)




