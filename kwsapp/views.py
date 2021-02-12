from . import app
from flask import flash, redirect, render_template, url_for
from . import login_manager
from flask_login import current_user, login_required, login_user, logout_user
from .resources import add_user, users_list, user_exist
from .forms import SignupForm, LoginForm
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
# @login_required
def base():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        if current_user.is_authenticated:
            return redirect(url_for('login'))

        if user and user.verify_password(password):

            login_user(user, remember=False)
            # print(current_user.name)
            return redirect(url_for('base'))

        else:

            flash('This user does not exist or the password is incorrect.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # print(current_user.name, current_user.is_authenticated)
    logout_user()
    # TODO: Need to check why the session remembers the user after closing the browser.
    # print(current_user.is_authenticated)
    return redirect(url_for('login'))


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
