from flask import render_template, request, session, jsonify, url_for, redirect
from forms.forms import signUpForm
#import app
from app import app,db
import models
import requests
app.config['CORS_HEADERS'] = 'application/json'

@app.errorhandler(404)
def Er404(error):
    #return render_template("error_404.html"), 404
    return render_template("/errors/404.html"), 404
@app.route("/append-list")
def append_coins():
    pass
@app.route("/")
def Homepage():
    table_data = models.Coins_Table.query.all()
    data=[
        {
            "name":"BTC",
            "price":"40000",
            "daypercent":"+0.1",
            "marketcap":"1,000,000,000",
            "vol":"26000"
        },
        {
            "name":"ETH",
            "price":"4000",
            "daypercent":"+2.1",
            "marketcap":"1,000,000",
            "vol":"15k"
        },
        {
            "name":"USDT",
            "price":"1",
            "daypercent":"-0.01",
            "marketcap":"1,000,000",
            "vol":"10k"
        }
    ]
    return render_template("index.html",data=table_data)

@app.route("/coin/<coin_name>")
def coin_inner(coin_name):
    return redirect(url_for('CallGecko',coin_name = coin_name))

def BTC_Page(coin_name):
    coin_name=coin_name.upper()
    if models.Coins_Table.query.filter_by(ShortName=coin_name).first() is not None:
        print("ok")
    Coin=models.Coins_Table.query.filter_by(ShortName=coin_name).first()
    Info_dict={
        'Fullname':Coin.FullName,
        'Shortname':Coin.ShortName
    }
    return render_template("inner.html",coin_name=coin_name,info=Info_dict)

def api_call_manual(fromDate, fromTime , TimeStamp):
    '''fromDate = 2022-01-01
       fromTime = 00:00:00'''
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T00:00:00&time_end=2021-12-24T23:59:00'
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T16:00:00'
    headers = {'X-CoinAPI-Key' : 'CECC7DA6-25B4-4F99-A8C3-DD810E21AD48'}
    baseurl = f'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id={TimeStamp}HRS&time_start={fromDate}T{fromTime}'
    response = requests.get(baseurl, headers=headers)
    data = response.json()
    #return baseurl
    return str(data)

def api_call():
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T00:00:00&time_end=2021-12-24T23:59:00'
    #url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-01-10T16:00:00'
    url = 'https://rest.coinapi.io/v1/ohlcv/BINANCE_SPOT_BTC_USDT/history?period_id=1HRS&time_start=2022-03-29T00:00:00'
    headers = {'X-CoinAPI-Key' : 'CECC7DA6-25B4-4F99-A8C3-DD810E21AD48'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data
def api_call_test():
    url = 'http://api.open-notify.org/astros.json'
    #headers = {'X-CoinAPI-Key' : 'CECC7DA6-25B4-4F99-A8C3-DD810E21AD48'}
    response = requests.get(url)
    data = response.json()
    return data
@app.route("/priceapi", methods=["GET"])
def api():
    dic1=api_call()
    data = {"datas":dic1}
    return  data
@app.route("/apii", methods=["GET"])
def apii():
    dic1=[{
    "high": 2,
    "open": 1.2,
    "close": 1.5,
    "low": 1},
    {"high": 3,
    "open": 1.3,
    "close": 1.6,
    "low": 1.2}
    ]
    dic2=jsonify(dic1)
    dic2.headers.add("Access-Control-Allow-Origin", "*")
    return  dic2
@app.route("/run", methods=["GET"])
def run_route():
    dic1=api_call()
    logs=[]
    for i in range(len(dic1)):
        try:
            BTC_Price =models.BTC_prc(time_Open=dic1[i]["time_period_start"],Open=dic1[i]["price_open"],Close=dic1[i]["price_close"],High=dic1[i]["price_high"],Low=dic1[i]["price_low"],Volume=dic1[i]["volume_traded"],trades_Count=dic1[i]["trades_count"])
            db.session.add(BTC_Price)
            db.session.commit()
            a= str(i) + " : با موفقیت اضافه شد"
            logs+=[a]
        except Exception as e:
            a=str(i) + " : مشکلی رخ داد"
            logs+= [a]
    return render_template("log.html",logs=logs)

@app.route("/run1")
def run_route1():
    dic1=api_call()
    logs=[]
    for i in dic1:
        try:
            BTC_Price =models.BTC_prc(time_Open=i["time_period_start"],Open=i["price_open"],Close=i["price_close"],High=i["price_high"],Low=i["price_low"],Volume=i["volume_traded"],trades_Count=i["trades_count"])
            db.session.add(BTC_Price)
            db.session.commit()
            a= str(i["time_period_start"][11:16]) + " : با موفقیت اضافه شد"
            logs+=[a]
        except Exception as e:
            a=str(i) + " : مشکلی رخ داد"
            logs+= [a]
    return render_template("log.html",logs=logs)

@app.route("/logger", methods=["GET"])
def logger():
    logs=["hello","Yellow"]
    i=0
    a= str(i) + " : با موفقیت اضافه شد"
    logs+=[a]
    return render_template("log.html",logs=logs)

@app.route("/logg")
def logg():
    dic1=api_call()
    BTC_Price =models.BTC_prc(time_Open=dic1[0]["time_period_start"],Open=dic1[0]["price_open"],Close=dic1[0]["price_close"],High=dic1[0]["price_high"],Low=dic1[0]["price_low"],Volume=dic1[0]["volume_traded"],trades_Count=dic1[0]["trades_count"])
    db.session.add(BTC_Price)
    db.session.commit()
    if BTC_Price:
        return True
    else:
        return False

@app.route("/last-L")
def lastBtcPrice():
    #lastPrice=session.query(cmsapp.models.BTC_prc).order_by(cmsapp.models.BTC_prc.id.desc()).first()
    #lastPrice = cmsapp.models.BTC_prc.query.all()
    lastIndex = models.BTC_prc.query.count()
    lastTime = models.BTC_prc.query.filter_by(id=lastIndex).first()
    #return str(lastTime.time_Open)
    return str(lastIndex)

@app.route("/testm")
def manualtest():
    return api_call_manual('2022-01-16','00:00:00',1)
@app.route("/test-m", methods=['GET'])
def man_test():
    fromDate = request.args.get('from')
    fromTime = request.args.get('time')
    ts= request.args.get('timestamp')
    '''2022-01-01
       fromTime = 00:00:00'''
    return api_call_manual(fromDate,fromTime,ts)
@app.route("/chart-test")
def chartTest():
    recordsList=models.BTC_prc.query.all()
    recordsDic=[]
    # for i in recordsList:
    #     recordsDic+=[{
    #     "time_period_start":i[time_Open],
    #     "price_open":i[Open],
    #     "price_close":i[Close],
    #     "price_high":i[High],
    #     "price_low":i[Low],
    #     "volume_traded":i[Volume],
    #     "trades_count":i[trades_Count]
    #     }]
    for i in recordsList:
        recordsDic+=[{
        "time_period_start":i.time_Open,
        "price_open":i.Open,
        "price_close":i.Close,
        "price_high":i.High,
        "price_low":i.Low,
        "volume_traded":i.Volume,
        "trades_count":i.trades_Count
        }]
    # recordsDic+=[recordsList[0]["time_Open"]]
    rDic=jsonify(recordsDic)
    rDic.headers.add("Access-Control-Allow-Origin", "*")
    # return jsonify(recordsDic)
    return rDic

#@app.rout("/svelte")
#def svl():
    #return send_from_directory('C:\Users\saleh\Downloads\notus-svelte-main\notus-svelte-main\public','index.html')
@app.route("/eth-call")
def ETHCall():
    dic1={}
    r=requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=truehttps://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true',data=dic1)
    data = r.json()
    print(data)
    return(data)

#TODO: ADD MANUAL API CALL A TRY CATCH
@app.route("/form-signup",methods=['GET'])
def suPForm():
    name=None
    form=signUpForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
    return render_template('auth/sign-up.html',form=form,name=name)

@app.route("/form-signup",methods=['POST'])
def suPFormPOST():
    return "ok"
from CoinMarketCap import CoinMarketCap
@app.route("/table_0")
def tablefunc():
    CoinMarketCap_data = CoinMarketCap.listing()
    previous = models.Coins_Table.query.all()
    # db.session.delete(previous)
    models.Coins_Table.query.delete()
    for i in range(len(CoinMarketCap_data['data'])):
        coin_item =  models.Coins_Table(ShortName=CoinMarketCap_data['data'][i]["symbol"],FullName=CoinMarketCap_data['data'][i]["name"],price=CoinMarketCap_data['data'][i]["quote"]["USD"]["price"],percent=CoinMarketCap_data['data'][i]["quote"]["USD"]["percent_change_24h"],marketcap=CoinMarketCap_data['data'][i]["quote"]["USD"]["market_cap"],volume=CoinMarketCap_data['data'][i]["quote"]["USD"]["volume_24h"])
        db.session.add(coin_item)
        db.session.commit()
    return "ookk"
@app.route("/line-chart")
def linechart():
    chart_data = models.BTC_prc.query.all()
    return render_template("chart/ch.html",data=chart_data)
@app.route("/line-chart0")
def linechart0():
    return render_template("chart/ch1.html")
@app.route("/map")
def market_Map():
    coin_data = models.Coins_Table.query.all()
    return render_template("chart/ch3.html",coin_data=coin_data)
@app.route("/expectation")
@app.route("/expectation/")
def expectationPage():
    query = db.select(
    models.expectation.ShortName).group_by(models.expectation.ShortName)
    coins_list = db.engine.execute(query).fetchall()
    # coins=models.expectation.query.group_by(ShortName).all()
    coins_names=[coin[0] for coin in coins_list]
    print("--------------\n----------------",coins_names)
    query='select * from Coins__Table INNER JOIN expectation ON Coins__Table.ShortName=expectation.ShortName GROUP BY expectation.ShortName ORDER BY Coins__Table.marketcap Desc'
    # details=models.Coins_Table.query.join(models.expectation.ShortName=models.Coins_Table.ShortName).all()
    # details=db.session.query(models.Coins_Table).join(models.Coins_Table.ShortName==models.expectation.ShortName)
    details=db.engine.execute(query)
    detail = [(row[1],row[2],row[3],row[4],row[5],row[6]) for row in details]
    # details=list(details.fetchall())
    print(detail)
    return render_template('expectation/list.html',coins=coins_names,details=detail)
@app.route("/expectation/<coin_name>")
def expectation_page(coin_name):
    from sqlalchemy import or_
    # coin_name=coin_name.upper()
    # Coin=models.Coins_Table.query.filter_by(ShortName=coin_name).first()
    Coin = models.Coins_Table.query.filter(
    or_(models.Coins_Table.ShortName.ilike(coin_name),models.Coins_Table.FullName.ilike(coin_name))
    ).first()
    data=models.Expectation_Finder(Coin.ShortName)
    # Coin_data=models.exec(Coin.upper())_price.query.all()
    # print(Coin_data)

    return render_template('expectation/index.html',data=data,Coin=Coin)
@app.route("/trending")
def trending():
    return render_template('trending.html')
@app.route("/indicators")
def indicatorsTutorial():
    return render_template('indicators.html')
@app.route("/indicator")
def indicatorTutorial():
    return render_template('indicator.html')
#_________________TEST_________________
@app.route("/news-append")
def appendNews():
    from datetime import datetime, timedelta
    for i in range(3):
        Article=models.Article.query.filter_by(id=(i+1)).first()
        Article.articleDate=datetime.today() - timedelta(days=1)
        db.session.add(Article)
        db.session.commit()
    return "ok"
@app.route("/cards-test")
def testfunc():
    coins=models.Coins_Table.query.limit(6).all()
    return render_template("cards/cards.html",coins=coins)

@app.route("/callgecko-test/<coin_name>")
def CallGecko(coin_name):
    from sqlalchemy import and_, or_, not_
    coin_name=coin_name.upper()
    # Coin=models.Coins_Table.query.filter_by(ShortName=coin_name).first()
    
    Coin = models.Coins_Table.query.filter(
    or_(models.Coins_Table.ShortName.ilike(coin_name),models.Coins_Table.FullName.ilike(coin_name))
    ).first()
    import CoinGecko
    Chart_Data=CoinGecko.Caller(Coin.FullName)
    # coin_data = models.Coins_Table.query.all()
    coin_data=models.UsualInfo.query.filter_by(ShortName=Coin.ShortName).first()
    # Chart_Data=[]
    '''
    if models.Coins_Table.query.filter_by(ShortName=coin_name).first() is not None:
        print("ok")
    '''
    Info_dict={
        'Fullname':Coin.FullName,
        'Shortname':Coin.ShortName
    }
    # return render_template("test/inner.html",Coin=Coin,info=Info_dict,Chart_Data=Chart_Data)
    return render_template("inner/base.html",Coin=Coin,info=Info_dict,Chart_Data=Chart_Data,coin_data=coin_data)
import CoinGecko
@app.route("/callgecko-test/")
def CallGecko_pure():
    coin_name='btc'
    try:
        Coin_Data=CoinGecko.Caller(coin_name)
    except Exception as e:
        return e
    return jsonify(Coin_Data)
#TODO: complete usual information of the coin table
#TODO: schedule api call
#______________________________TEST_____________________________________
@app.route("/blog")
def BlogIndex():
    data=models.indicatorArticle.query.all()
    return render_template('blog/index.html',data=data)
@app.route("/blog/<indicator>")
def indicator_article(indicator):
    indicator=indicator.lower()
    data=models.indicatorArticle.query.filter_by(name=indicator).first()
    if data is not None:
        return render_template('blog/single.html',data=data)
    else:
        return render_template("/errors/404.html"), 404
@app.route("/most-24h-change")
def most24hChange():
    # table_data = models.Coins_Table.query.order_by(models.Coins_Table.percent.desc()).all()
    table_data = models.Coins_Table.query.order_by(models.Coins_Table.percent.desc()).all()
    return render_template("index.html",data=table_data)
@app.route("/coin-api-caller/<coin>")
def api_caller_coin(coin):
    return models.api_add_commit(coin.upper())
@app.route("/last-update-checker/<name>")
def func01(name):
    from datetime import datetime,timedelta
    name=name.upper()
    #models.DataUpdates.query.filter_by(name=name).order_by(models.DataUpdates.id.desc()).first().
    try:
        last_update=models.expectation.query.filter_by(ShortName=name).order_by(models.expectation.id.desc()).first()
        last_update=last_update.time_Open
        date_time_obj = datetime.strptime(last_update[:-2], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d")
    except:
        pass
    today=datetime.today().strftime("%Y-%m-%d")
    try:
        if last_update==None or date_time_obj!=today:
            old_records=models.expectation.query.filter_by(ShortName=name).all()
            for record in old_records:
                db.session.delete(record)
            db.session.commit()
            models.api_add_commit(name)
            return str("ok")
        else:
            records=models.expectation.query.filter_by(ShortName=name).all()
            return str(records)
    except Exception as e:
        return str(e)
'''
@app.route("/in2")
def index2hndl():
    table_data = models.Coins_Table.query.all()
    article_data = models.Article.query.all()
    return render_template("index2.html",data=table_data,article=article_data)
'''