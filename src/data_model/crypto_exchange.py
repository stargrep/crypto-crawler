from simple_model import Model


class CryptoExchange(Model):
    id: int
    exchange: str
    web_site: str
    start_at_milli: int
    end_at_milli: int
    location: str
    status: str
