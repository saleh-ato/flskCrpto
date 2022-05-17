from flask import Flask, render_template, request, make_response, session, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)
app.config['SECRET_KEY'] = 'lssr9j4tc9eyliz66nxur8l9rv4naai4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

filedir=os.path.dirname(os.path.abspath(__file__))
goalroute=os.path.join(filedir,"app.db")
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+goalroute

UPLOAD_FOLDER = os.path.join(filedir,"uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/uploads/<path:path>")
@app.route("/images/<path:path>")
def static_dir(path):
    path=path.lower()
    return send_from_directory("uploads", path)

db= SQLAlchemy(app)
migrate = Migrate(app, db)

import models
import views
#import flskcrpt.userviews

import time
import atexit
from SchedulE import check_all
from apscheduler.schedulers.background import BackgroundScheduler

'''
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
'''

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_all, trigger="interval", minutes=15)
#scheduler.add_job(func=check_all, trigger="interval", minutes=1)
scheduler.start()