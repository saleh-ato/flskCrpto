import models
from app import db
from datetime import datetime
from ApiDrivers import CoinMarketCap 
EXPECTATION=["BTC","BNB","ETH","XRP","SOL","ADA","AVAX"]#,"LUNA"]
class DataUpdateChecker:
    def Expectation_(self,name):
        from datetime import datetime
        name=name.upper()
        try:
            last_update=models.expectation.query.filter_by(ShortName=name).order_by(models.expectation.id.desc()).first()
            last_update=last_update.time_Open
            date_time_obj = datetime.strptime(last_update[:-2], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d")
        except:
            # if there isn't data of that naem 
            pass
        today=datetime.today().strftime("%Y-%m-%d")
        try:
            if last_update==None or date_time_obj!=today:
                # if isn't update
                old_records=models.expectation.query.filter_by(ShortName=name).all()
                for record in old_records:
                    db.session.delete(record)
                db.session.commit()
                # deleted old records
                models.api_add_commit(name)
                # new recods add and commit
                return str("ok")
            else:
                records=models.expectation.query.filter_by(ShortName=name).all()
                return str(len(records))
        except Exception as e:
            return str(e)
    def Coins_Table_data(self):
        try:
            update_object=models.DataUpdates.query.filter_by(name="Coins_Table").first()
        except:
            pass
        if (update_object is None):
            models.Coins_Table.query.delete()
            CoinMarketCap_data = CoinMarketCap.listing()
            for i in range(len(CoinMarketCap_data['data'])):
                coin_item =  models.Coins_Table(ShortName=CoinMarketCap_data['data'][i]["symbol"],FullName=CoinMarketCap_data['data'][i]["name"],price=CoinMarketCap_data['data'][i]["quote"]["USD"]["price"],percent=CoinMarketCap_data['data'][i]["quote"]["USD"]["percent_change_24h"],marketcap=CoinMarketCap_data['data'][i]["quote"]["USD"]["market_cap"],volume=CoinMarketCap_data['data'][i]["quote"]["USD"]["volume_24h"])
                db.session.add(coin_item)
                db.session.commit()
            models.Last_Update_Log("Coins Table")
            return "Coins Table Updated."
        elif(update_object.LastUpdate != str(datetime.now().strftime("%Y-%m-%d"))):
            CoinMarketCap_data = CoinMarketCap.listing()
            models.Coins_Table.query.delete()
            for i in range(len(CoinMarketCap_data['data'])):
                coin_item =  models.Coins_Table(ShortName=CoinMarketCap_data['data'][i]["symbol"],FullName=CoinMarketCap_data['data'][i]["name"],price=CoinMarketCap_data['data'][i]["quote"]["USD"]["price"],percent=CoinMarketCap_data['data'][i]["quote"]["USD"]["percent_change_24h"],marketcap=CoinMarketCap_data['data'][i]["quote"]["USD"]["market_cap"],volume=CoinMarketCap_data['data'][i]["quote"]["USD"]["volume_24h"])
                db.session.add(coin_item)
                db.session.commit()
            models.Last_Update_Log()
            return "Coins Table Updated."
        elif(update_object is not None):
            return update_object.LastUpdate
def check_all():
    checker=DataUpdateChecker()
    for name in EXPECTATION:
        print(checker.Expectation_(name))
    print(checker.Coins_Table_data())