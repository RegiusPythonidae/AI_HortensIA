import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_NAME = "Hortensia"

    # Flask settings

    CSRF_ENABLED = True
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = "Cannottell"

    # Flask SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-User settings
    USER_APP_NAME = 'Hortensia'
    USER_ENABLE_EMAIL = True
    USER_ENABLE_CONFIRM_EMAIL = False
    USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = True
    USER_SEND_REGISTERED_EMAIL = True
    USER_AUTO_LOGIN_AT_LOGIN = True
    USER_AUTO_LOGIN_AFTER_CONFIRM = True

    USER_REGISTER_URL = '/register'
    USER_LOGIN_URL = '/'

    USER_LOGIN_TEMPLATE = 'flask_user/login_or_register.html'
    USER_REGISTER_TEMPLATE = 'flask_user/login_or_register.html'

    USER_AFTER_LOGIN_ENDPOINT = 'tickets.tickets'

    USER_ENABLE_RETYPE_PASSWORD = False

    # Flask-Babel settings

    BABEL_DEFAULT_LOCALE = 'ka'
    BABEL_DOMAIN = 'messages'
