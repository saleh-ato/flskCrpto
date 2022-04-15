import requests
exceptions={
    'xrp':'ripple',
    'bnb':'binancecoin',
    'usd coin':'usd-coin',
    'terra':'terra-luna',
    'avalanche':'avalanche-2',
    'binance usd':'binance-usd',
    'shiba inu':'shiba-inu',
    'wrapped bitcoin':'wrapped-bitcoin',
    'near protocol':'near',
    'polygon':'matic-network',
    'cronos':'crypto-com-chain',
    'bitcoin cash':'bitcoin-cash',
    'ftx token':'ftx-token',
    'unus sed leo':'leo-token',
    'ethereum classic':'ethereum-classic',
    'internet computer':'internet-computer',
    'hedera':'hedera-hashgraph',
    'elrond':'elrond-erd-2',
    'the sandbox':'the-sandbox',
    'theta network':'theta-token',
    'axie infinity':'axie-infinity',
    'klaytn':'klay-token'
}
def Caller(coin_name):
    dic1={}
    coin_name=coin_name.lower()
    try:
        coin_name=exceptions[coin_name]
    except:
        pass

    #r=requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=truehttps://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true',data=dic1)
    r=requests.get('https://api.coingecko.com/api/v3/coins/%s/ohlc?vs_currency=usd&days=7'%coin_name,data=dic1) #1/7/14/30/90/180/365/max
    print('https://api.coingecko.com/api/v3/coins/%s/ohlc?vs_currency=usd&days=7'%coin_name)
    data = r.json()
    return data