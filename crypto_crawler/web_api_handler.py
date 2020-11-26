# import requests
# from crypto_crawler.const import WEB_API_EXCHANGE_PRICE_URL, COIN_NAME_BITCOIN, TARGET_EXCHANGE_ID
# from crypto_crawler.common import get_system_milli, milli_to_datetime_str
#
#
# def query_price(exchange_id: str) -> CryptoPrice:
#     response = requests.get(WEB_API_EXCHANGE_PRICE_URL + exchange_id)
#     current_time = get_system_milli()
#     data = response.json()['data']
#     quote = response.json()['data']['market_pairs'][0]['quote']['exchange_reported']
#     return CryptoPrice(exchange=data['name'],
#                        coin_name=COIN_NAME_BITCOIN,
#                        price=quote['price'],
#                        pricing_time_str=milli_to_datetime_str(current_time),
#                        pricing_time=current_time,
#                        volume=quote['volume_24h_base'],
#                        volume_p=quote['volume_24h_base'],
#                        fee_type='PERCENTAGE',
#                        coin_pair='BTC/USDT')
#
#
# def get_web_content(target_exchange_ids: [int] = TARGET_EXCHANGE_ID) -> [CryptoPrice]:
#     return [query_price(str(eid)) for eid in target_exchange_ids]

