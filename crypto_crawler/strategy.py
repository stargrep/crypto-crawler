import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA

from crypto_crawler.const import TRANS_FEE_PERCENTAGE_AVG, SELECT_CRYPTO_RECENT_500
from crypto_crawler.reporting import write_as_new_file, read_as_df, plot_train_and_test, plot_prediction, \
    plot_validation
from crypto_crawler.sql_utils import read


def arbitrage_signal(prices, fee_value=TRANS_FEE_PERCENTAGE_AVG):
    """
    # https://www.investopedia.com/terms/t/trade-signal.asp

    apply second best arbitrage with ok profit
    :param fee_value:
    :param prices:
    :return:
    """
    prices.sort(key=lambda price: price.price)
    buy = prices[0]
    sell = prices[-1]
    avg_profit = (sell.price * (1 - fee_value) - buy.price * (1 + fee_value))
    avg_profit_p = avg_profit / 2 / sell.price * 100

    return {
        "profit_p": avg_profit_p,
        "profit_value": avg_profit,
        "total_fee_p": fee_value * 2 * 100,
        "buy": buy,
        "sell": sell
    }


def create_crypto_file(db_name):
    """
    train : test = 4 : 1
    400 100 records
    :return:
    """
    crypto_list = read(SELECT_CRYPTO_RECENT_500, db_name)
    # add time str to the result.
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
    :return: list of prediction
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
        model = ARIMA(history, order=(2, 0, 2))
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
    score = score_with_diff(test_ar.tolist(), predictions, 0.05, 0)    # 5 cents
    return score
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
    total_val = 100000  # account initial values
    for i in range(len(pred_list)):
        if pred_list[i] < baseline * (1 - fee_p) and inventory < 10:
            inventory += 1
            earning -= test_list[i] * (1 + fee_p)
        elif pred_list[i] > baseline * (1 + fee_p) and inventory > 0:
            inventory -= 1
            earning += test_list[i] * (1 - fee_p)

    return earning + inventory * test_list[-1]
