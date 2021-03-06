from . import app
from flask import flash, redirect, render_template, url_for
from . import login_manager
from flask_login import current_user, login_required, login_user, logout_user
from .resources import add_user, users_list, user_exist
from .forms import SignupForm, LoginForm
from . import models


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(user_id)


@app.route('/')
# @login_required
def base():
    return render_template('base.html')


@app.route('/welcome')
# @login_required
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        user = models.User.query.filter_by(email=email).first()

        if current_user.is_authenticated:
            return redirect(url_for('login'))

        if user and user.verify_password(password):

            if not user.email_confirmed:
                flash('Your email address has not yet been verified. '
                      'Please check your email for a letter with a confirmation link.', 'danger')
                return redirect(url_for('login'))

            login_user(user, remember=False)
            # print(current_user.name)
            return redirect(url_for('base'))

        else:

            flash('This user does not exist or the password is incorrect.', 'danger')

    return render_template('login.html', form=form, name=None)


@app.route('/logout', methods=['GET'])
def logout():

    logout_user()
    # TODO: Need to check why the session remembers the user after closing the browser.
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
