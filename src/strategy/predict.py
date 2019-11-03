import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

from src.common.app_sql import SELECT_CRYPTO_RECENT_500
from src.data_model import CryptoPrice
from src.data_storage.pgsql_util import get_data
from src.reporting import write_as_new_file
from src.reporting.file_util import read_as_df
from src.reporting.plot_util import plot_train_and_test, plot_prediction, plot_validation


def create_crypto_file():
    """
    train : test = 4 : 1
    400 100 records
    :return:
    """
    crypto_list = get_data(SELECT_CRYPTO_RECENT_500)
    write_as_new_file("total.csv", crypto_list, CryptoPrice.get_col_list())
    train = crypto_list[0:int(len(crypto_list)*0.8)]    # 80%
    test = crypto_list[int(len(crypto_list)*0.8):]  # 20%
    write_as_new_file("train.csv", train, CryptoPrice.get_col_list())
    write_as_new_file("test.csv", test, CryptoPrice.get_col_list())


def mse(y_true, y_pred):
    """
    error functions: Mean Squared Error (MSE)
    :return:
    """
    return mean_squared_error(y_true, y_pred)


def smape(y_true, y_pred):
    """
    Symmetric Mean Absolute Percentage Error (SMAPE).
    SMAPE is commonly used as an accuracy measure based on relative errors

    :return:
    """
    return np.mean((np.abs(y_pred - y_true) * 200 / (np.abs(y_pred) + np.abs(y_true))))


def arima():
    """
    ARIMA (AutoRegressive Integrated Moving Average)
    :return:
    """
    df = read_as_df("total.csv")
    train_data, test_data = df[0:int(len(df) * 0.8)], df[int(len(df) * 0.8):]
    df.head()
    plot_train_and_test(train_data, test_data, df)
    train_ar = train_data['price'].values
    test_ar = test_data['price'].values

    history = [x for x in train_ar]
    print(type(history))

    predictions = list()
    for t in range(len(test_ar)):
        model = ARIMA(history, order=(3, 1, 0))
        model_fit = model.fit(disp=0)
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test_ar[t]
        history.append(obs)

    plot_prediction(df, test_data, predictions)

    return predictions


def arima_validation(predictions):
    df = read_as_df("total.csv")
    train_data, test_data = df[0:int(len(df) * 0.8)], df[int(len(df) * 0.8):]

    test_ar = test_data['price'].values
    #error = mean_squared_error(test_ar, predictions)
    #print('Testing Mean Squared Error: %.3f' % error)
    #error2 = smape(test_ar, predictions)
    #print('Symmetric mean absolute percentage error: %.3f' % error2)

    plot_validation(df, test_data, predictions)
    score_with_diff(test_ar.tolist(), predictions, 0.05, 0)    # 5 cents
    # smaller than 2% then consider the result is correct


def score_with_diff(test_list, pred_list, limit, lag):
    size = len(test_list) - lag
    score = 0
    for i in range(size):
        if abs(test_list[i] - pred_list[i + lag]) < limit:
            score += 1
    return score / size


def earning_calculation(pred_list, fee_p):
    df = read_as_df("total.csv")
    train_data, test_data = df[0:int(len(df) * 0.8)], df[int(len(df) * 0.8):]

    train_arr = test_data['price'].values
    test_list = test_data['price'].values.tolist()

    # calculation
    baseline = np.mean(train_arr)
    inventory = 0
    earning = 0
    for i in range(len(pred_list)):
        if pred_list[i] < baseline * (1 - fee_p) and inventory < 10:
            inventory += 1
            earning -= test_list[i] * (1 + fee_p)
        elif pred_list[i] > baseline * (1 + fee_p) and 0 < inventory:
            earning += test_list[i] * (1 - fee_p)

    return earning + inventory * test_list[-1]
