import matplotlib.pyplot as plt
import numpy as np


def plot_train_and_test(train_data, test_data, total_data):
    """
    plot train and test set data as data frame
    :param train_data: dataframe
    :param test_data: dataframe
    :param total_data: dataframe
    :return: void
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


def plot_prediction(df, test_data, predictions):
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


def plot_validation(df, test_data, predictions):
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

