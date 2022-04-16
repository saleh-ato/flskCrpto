from flask import render_template, request, session, jsonify, url_for, redirect
from forms.forms import signUpForm
from app import app,db
import models
import requests
app.config['CORS_HEADERS'] = 'application/json'

@app.errorhandler(404)
def Er404(error):
    return render_template("/errors/404.html"), 404

@app.route("/")
def Homepage():
    table_data = models.Coins_Table.query.all()
    return render_template("index.html",data=table_data)

@app.route("/coin/<coin_name>")
def coin_inner(coin_name):
    return redirect(url_for('CallGecko',coin_name = coin_name))

@app.route("/blog")
def BlogIndex():
    data=models.indicatorArticle.query.all()
    return render_template('blog/index.html',data=data)

@app.route("/expectation")
@app.route("/expectation/")
def expectationPage():
    query = db.select(
    models.expectation.ShortName).group_by(models.expectation.ShortName)
    coins_list = db.engine.execute(query).fetchall()
    coins_names=[coin[0] for coin in coins_list]
    print("--------------\n----------------",coins_names)
    query='select * from Coins__Table INNER JOIN expectation ON Coins__Table.ShortName=expectation.ShortName GROUP BY expectation.ShortName ORDER BY Coins__Table.marketcap Desc'
    details=db.engine.execute(query)
    detail = [(row[1],row[2],row[3],row[4],row[5],row[6]) for row in details]
    return render_template('expectation/list.html',coins=coins_names,details=detail)

@app.route("/expectation/<coin_name>")
def expectation_page(coin_name):
    from sqlalchemy import or_
    Coin = models.Coins_Table.query.filter(
    or_(models.Coins_Table.ShortName.ilike(coin_name),models.Coins_Table.FullName.ilike(coin_name))
    ).first()
    data=models.Expectation_Finder(Coin.ShortName)
    return render_template('expectation/index.html',data=data,Coin=Coin)

@app.route("/trending")
def trending():
    return render_template('trending.html')

@app.route("/map")
def market_Map():
    coin_data = models.Coins_Table.query.all()
    return render_template("chart/ch3.html",coin_data=coin_data)

@app.route("/callgecko-test/<coin_name>")
def CallGecko(coin_name):
    from sqlalchemy import and_, or_, not_
    coin_name=coin_name.upper()
    Coin = models.Coins_Table.query.filter(
    or_(models.Coins_Table.ShortName.ilike(coin_name),models.Coins_Table.FullName.ilike(coin_name))
    ).first()
    import CoinGecko
    Chart_Data=CoinGecko.Caller(Coin.FullName)
    coin_data=models.UsualInfo.query.filter_by(ShortName=Coin.ShortName).first()
    return render_template("inner/base.html",Coin=Coin,Chart_Data=Chart_Data,coin_data=coin_data)
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

#TODO: complete usual information of the coin table