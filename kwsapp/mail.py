from flask_mail import Message
from . import mail

message = Message('test subject', sender='xperia.t.mazurak@gmail.com', recipients=['masurak@ukr.net'])

message.body = 'text body'
message.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(message)
