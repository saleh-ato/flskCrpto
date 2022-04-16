import requests
from datetime import datetime, timedelta,timezone
def api_call(coin_name,date_time):
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T00:00:00&time_end=2021-12-24T23:59:00'
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T16:00:00'
    url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_%s_USDT/history?period_id=1HRS&time_start=%s' %(coin_name ,date_time)
    headers = {'X-CoinAPI-Key' : 'CECC7DA6-25B4-4F99-A8C3-DD810E21AD48'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
def api_call_helper(coin_name):
    coin_name=coin_name.upper()
    SubtractDays=2
    date_time=(datetime.now(timezone.utc) - timedelta(days=SubtractDays)).strftime('%Y-%m-%dT%H:%M:%S')
    # print("----------",date_time)
    # date_time=str(date_time.replace(hour=0,minute=0,second=0).isoformat()[:-7])
    return api_call(coin_name,date_time)

# print(api_call_helper('btc'))