from flask import render_template, session, redirect, url_for, current_app, request, flash
from . import main
from ..models import db
from config import URI
from sqlalchemy_utils import database_exists, create_database

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/createdb/', methods=['GET', 'POST'])
def createdb():
    if not database_exists(URI):
        create_database(URI)
    print("資料庫已經存在")
    db.create_all()
    return redirect(url_for("main.index"))

@main.route('/dashboard/')
def dashboard():
    return render_template("echarts.html")

@main.route('/reserve/')
def reserve():
    return render_template("reserve.html")

@main.route('/about_us/')
def about_us():
    return render_template("about_us.html")

@main.route('/today2/')
def today2():
    return render_template("today2.html")

@main.route('/calendar_right/')
def calendar_right():
    return render_template("calendar_right.html")

