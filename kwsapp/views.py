from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from . import app
from . import login_manager
from .models import User
from .forms import SignupForm, LoginForm
from .resources import add_user, users_list, user_exist


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
@login_required
def base():
    return render_template('base.html')


@app.route('/email_confirm/<token>')
@login_required
def email_confirm(token):
    if current_user.role.name == 'guest':
        flash('Current user Guest', 'info')
        return redirect(url_for('base'))
    if current_user.email_confirm(token):
        flash('You have confirmed your email.', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'danger')

    return render_template('welcome.html')


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

        user = User.query.filter_by(email=email).first()

        if current_user.is_authenticated:
            return redirect(url_for('base'))

        if user and user.verify_password(password):

            # if not user.email_confirmed:
            #     flash('Your email address has not yet been verified. '
            #           'Please check your email for a letter with a confirmation link.', 'danger')
            #     return redirect(url_for('login'))

            login_user(user, remember=False)

            next_url = request.args.get('next')

            if not next_url or url_parse(next_url).netloc != '':
                return redirect(url_for('base'))

            return redirect(next_url)

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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    # checks if a form has been submitted and validated
    if form.validate_on_submit():
        # get values from a form
        username = form.username.data
        email = form.email.data
        if user_exist(username, email):
            flash('Username or email address already exists', 'danger')
            return redirect(url_for('signup'))
        else:
            password = form.password.data
            add_user(username, email, password)
        return redirect(url_for('welcome'))

    return render_template('signup.html', form=form)


@app.route('/email')
def email():
    return render_template('mail/email.html')
