from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
class CoinMarketCap():
    def listing():
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
        'start':'1',
        'limit':'50',
        'convert':'USD'
        }
        #here you enter coin_market_cap  API Key
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'API Key',
        }
        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url,params=parameters)
            data = response.json()
            # from .. import models
            # from ..app import db
            # for i in range(len(data['data'])):
            #     coin_item =  models.Coins_Table(ShortName=data['data'][i]["symbol"],FullName=data['data'][i]["name"],price=data['data'][i]["quote"]["USD"]["price"],percent=data['data'][i]["quote"]["USD"]["percent_change_24h"],marketcap=data['data'][i]["quote"]["USD"]["market_cap"],volume=data['data'][i]["quote"]["USD"]["volume_24h"])
            #     db.session.add(coin_item)
            #     db.session.commit()
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)