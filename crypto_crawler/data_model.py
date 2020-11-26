from simple_model import Model


class StockPrice(Model):
    code: str
    trade_at: int
    trade_at_str: str
    open: float
    close: float
    high: float
    low: float
    volume: int

    def to_tuple(self):
        return (self.code, self.trade_at, self.trade_at_str,
                self.open, self.close, self.high, self.low, self.volume)

    @staticmethod
    def get_col_list():
        return ["code", "trade_time", "trade_time_str", "open", "close",
                "high", "low", "volume"]


class ProfitResult(Model):
    buy_at_str: str
    buy_price: float
    sell_at_str: str
    sell_price: float
    code: str
    count: int
    profit: float
    trading_fee: float


class StrategyResult(Model):
    code: str
    initial_asset: float
    start_at_str: str
    end_at_str: str
    profit_results: [ProfitResult]
    net_profit: float
    net_profit_p: float
    max_drawdown: float
    max_drawdown_p: float
    total_trade_number: int