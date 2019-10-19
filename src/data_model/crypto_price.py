from simple_model import Model


class CryptoPrice(Model):
    exchange: str
    coin_name: str
    price: float
    pricing_epoch_milli: int
    volume: int
    volume_p: float
    fee_type: str
    coin_pair: str
    is_active: bool = True
