from . import app
from flask import render_template
from .resources import users_list


@app.route('/')
def hello_world():
    # initial_settings()
    # print(url_for('static', filename='main.css'))
    return render_template('users_index.html', users=users_list())
    # return f'Hello World! {info}'


@app.route('/topnav')
def topnav():
    return render_template('users_tab.html', users=users_list())


@app.route('/admin/signup')
def signup():
    return render_template('signup.html')
