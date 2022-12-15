from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
babel = Babel()
bcrypt = Bcrypt()
login_manager = LoginManager()

extensions_list = [db, babel, bcrypt, login_manager]
