import pandas as pd
from os import path
import matplotlib.pyplot as plt
import numpy as np


from crypto_crawler.const import CSV_FOLDER_PATH


def write_as_new_file(file_name: str, data_list: [], column_list: []) -> None:
    full_path = path.join(CSV_FOLDER_PATH, file_name)
    df = pd.DataFrame(data_list, columns=column_list)
    df.to_csv(full_path, index=False)


def read_as_df(file_name: str) -> None:
    full_path = path.join(CSV_FOLDER_PATH, file_name)
    return pd.read_csv(full_path)


def plot_train_and_test(train_data: pd.DataFrame, test_data: pd.DataFrame, total_data: pd.DataFrame) -> None:
    """
    plot train and test set data as data frame
    """
    plt.figure(figsize=(12, 7))
    plt.title('Binance Bitcoin Prices')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.plot(train_data['price'], 'blue', label='Training Data')
    plt.plot(test_data['price'], 'green', label='Testing Data')
    plt.xticks(np.arange(0, 500, 50), total_data['time_epoch_milli'][0:500:50])
    plt.legend()
    plt.show()


def plot_prediction(df: pd.DataFrame, test_data: pd.DataFrame, predictions: np.array) -> None:
    plt.figure(figsize=(12, 7))
    plt.plot(df['price'], 'green', color='blue', label='Training Data')
    plt.plot(test_data.index, predictions, color='green', marker='o', linestyle='dashed',
             label='Predicted Price')
    plt.plot(test_data.index, test_data['price'], color='red', label='Actual Price')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.title('Prices Prediction')
    plt.xticks(np.arange(0, 500, 50), df['price'][0:500:50])
    plt.legend()
    plt.show()


def plot_validation(df: pd.DataFrame, test_data: pd.DataFrame, predictions: np.array) -> None:
    plt.figure(figsize=(12, 7))
    plt.plot(test_data.index, predictions, color='green', marker='o', linestyle='dashed', label='Predicted Price')
    plt.plot(test_data.index, test_data['price'], color='red', label='Actual Price')
    plt.legend()
    plt.title('Scoped Prices Prediction')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.xticks(np.arange(400, 500, 50), df['price'][400:500:50])
    plt.legend()
    plt.show()

# export data or pics to other formats
# PDF https://datatofish.com/export-matplotlib-pdf/
# EXCEL/POWERPOINT -> openpyxl
#     https://stackoverflow.com/questions/15177705/can-i-insert-matplotlib-graphs-into-excel-programmatically
# Or simply -> Jupyter Notebooks
