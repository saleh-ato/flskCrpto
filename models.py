from app import db
from ApiDrivers import coinapi

class DataUpdates(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(10))
    LastUpdate=db.Column(db.String(20))
class expectation(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    ShortName=db.Column(db.String(30))
    time_Open=db.Column(db.String(30))
    Open=db.Column(db.Float)
    Close=db.Column(db.Float)
    High=db.Column(db.Float)
    Low=db.Column(db.Float)
    Volume=db.Column(db.Float)
    trades_Count=db.Column(db.Integer)
class Coins_Table(db.Model):
    ''' coins of the first page '''
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    ShortName=db.Column(db.String(10))
    FullName=db.Column(db.String(20))
    price=db.Column(db.Float)
    percent=db.Column(db.Float)
    marketcap=db.Column(db.Float)
    volume=db.Column(db.Float)
class UsualInfo(db.Model):
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    ShortName=db.Column(db.String(10))
    Website=db.Column(db.String(45))
    Description=db.Column(db.Text)
    MaxSupply=db.Column(db.String(40))
    GitHubLink=db.Column(db.String(55))
class indicatorArticle(db.Model):
    id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    name=db.Column(db.String(20))
    description=db.Column(db.Text)
    shortdesc=db.Column(db.Text)

def api_add_commit(coin):
    coin_data=coinapi.api_call_helper(coin)
    try:
        for data in coin_data:
            # BTC_Price =models.BTC_prc(time_Open=dic1[i]["time_period_start"],Open=dic1[i]["price_open"],Close=dic1[i]["price_close"],High=dic1[i]["price_high"],Low=dic1[i]["price_low"],Volume=dic1[i]["volume_traded"],trades_Count=dic1[i]["trades_count"])
            row=expectation(ShortName=coin,time_Open=data["time_period_start"],Open=data["price_open"],Close=data["price_close"],High=data["price_high"],Low=data["price_low"],Volume=data["volume_traded"],trades_Count=data["trades_count"])
            # print(data)
            db.session.add(row)
            db.session.commit()
        return "True"
    except Exception as e:
        return "False "+str(e)

def Expectation_Finder(short_name):
    expect_data=expectation.query.filter_by(ShortName=short_name).all()
    return expect_data
def Last_Update_Log(name):
    from datetime import datetime
    old=DataUpdates.query.filter_by(name=name).first()
    if old is not None:
        db.session.delete(old)
        db.session.commit()
        newlog=DataUpdates(name=name,LastUpdate=str(datetime.now().strftime("%Y-%m-%d")))
        db.session.add(newlog)
        db.session.commit()