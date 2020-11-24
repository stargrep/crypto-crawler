from simple_model import Model


class CryptoExchange(Model):
    id: int
    exchange: str
    web_site: str
    start_at: int
    end_at: int
    country: str
    status: str


class CryptoPrice(Model):
    exchange: str
    coin_name: str
    price: float
    pricing_time_str: str = None
    pricing_time: int
    volume: int
    volume_p: float
    fee_type: str
    coin_pair: str

    def to_tuple(self):
        as_tuple = (self.exchange, self.coin_name, self.price,
                    self.pricing_time, self.volume, self.volume_p,
                    self.fee_type, self.coin_pair)
        return as_tuple

    @staticmethod
    def get_col_list():
        return ["id", "exchange", "coin_name", "price", "time",
                "volume", "volume_percentage", "fee_type", "coin_pair"]
