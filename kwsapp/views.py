from . import app, db
from .models import User, Role
from flask import render_template, url_for
from .resources import initial_settings, users_list


@app.route('/')
def hello_world():
    # initial_settings()
    # print(url_for('static', filename='main.css'))
    return render_template('users_index.html', users=users_list())
    # return f'Hello World! {info}'


@app.route('/topnav')
def topnav():
    return render_template('top-nav.html')
