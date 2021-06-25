# ----- App configuration section -----
SQLALCHEMY_DATABASE_URI = 'sqlite:///kws.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '777'
WTF_CSRF_ENABLED = False

# ----- Flask-Mail configuration section -----
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False

MAIL_USERNAME = 'xperia.t.mazurak@gmail.com'
MAIL_PASSWORD = 'perfecto777'

ADMIN_MAIL_USERNAME = 'KWS Admin <masurak@ukr.net>'
