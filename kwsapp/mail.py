# from itsdangerous import TimedJSONWebSignatureSerializer
from flask import render_template
from flask_mail import Message
from . import app, mail
from threading import Thread


# def send_email(user):
#     message = Message('test subject',
#                       sender=sender,
#                       recipients=['masurak@ukr.net', user.email])
#     message.body = 'text body'
#     message.html = render_template('email.html')
#
#     with app.app_context():
#         mail.send(message)
#
#     pass


def send_async_email(message):
    with app.app_context():
        mail.send(message)


def confirm_email_message(user):
    message = Message('KWS Please confirm your email address',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['masurak@ukr.net'])
    token = user.generate_email_confirm_token()
    message.html = render_template('mail/email.html', token=token)
    Thread(target=send_async_email, args=(message,)).start()


