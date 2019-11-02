from simple_model import Model


class CryptoPrice(Model):
    exchange: str
    coin_name: str
    price: float
    pricing_time_str: str = None
    pricing_epoch_milli: int
    volume: int
    volume_p: float
    fee_type: str
    coin_pair: str

    def to_tuple(self):
        as_tuple = (self.exchange, self.coin_name, self.price,
                    self.pricing_epoch_milli, self.volume, self.volume_p,
                    self.fee_type, self.coin_pair)
        return as_tuple

    @staticmethod
    def get_col_list():
        return ["id", "exchange", "coin_name", "price", "time_str", "time_epoch_milli",
                "volume", "volume_percentage", "fee_type", "coin_pair"]
