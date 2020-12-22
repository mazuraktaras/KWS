from . import app
from flask import flash, redirect, render_template, url_for
from .resources import users_list, user_exist
from .forms import SignupForm


@app.route('/')
def hello_world():
    # initial_settings()
    # print(url_for('static', filename='main.css'))
    return render_template('users_index.html', users=users_list())
    # return f'Hello World! {info}'


@app.route('/topnav')
def topnav():
    return render_template('users_tab.html', users=users_list())


@app.route('/admin/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # checks if form was submited and validated
    if form.validate_on_submit():
        # get values from form
        username = form.username.data
        email = form.email.data
        if user_exist(username, email):
            print('Login name or email already exist')
            return redirect(url_for('signup'))
        else:
            pass
        return redirect(url_for('topnav'))

    return render_template('signup.html', form=form)
