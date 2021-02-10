from . import app
from flask import flash, redirect, render_template, url_for
from . import login_manager
from flask_login import login_required, login_user
from .resources import add_user, users_list, user_exist
from .forms import SignupForm
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@login_required
def hello_world():
    # initial_settings()
    # print(url_for('static', filename='main.css'))
    return render_template('users_index.html', users=users_list())
    # return f'Hello World! {info}'


@app.route('/admin/users')
def users():
    return render_template('users_tab.html', users=users_list())


@app.route('/admin/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # checks if form was submitted and validated
    if form.validate_on_submit():
        # get values from form
        username = form.username.data
        email = form.email.data
        if user_exist(username, email):
            flash('Login name or email already exist', 'danger')
            return redirect(url_for('signup'))
        else:
            password = form.password.data
            add_user(username, email, password)
        return redirect(url_for('users'))

    return render_template('signup.html', form=form)
