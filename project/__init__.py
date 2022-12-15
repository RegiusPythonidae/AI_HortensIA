from flask import Flask
from flask_user import SQLAlchemyAdapter, UserManager
from project.extensions import extensions_list
from project.config import Config
from project.models import db
from project.models.user import User


def register_extensions(app):
    """Register extensions"""

    for extension in extensions_list:
        extension.init_app(app)

    # Register api (does not initialize otherwise)
    from project.api import api
    api.init_app(app)


def register_blueprints(app):
    from project.views.main.views import homepage_blueprint
    app.register_blueprint(homepage_blueprint, url_prefix="/")

    from project.views.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from project.views.tickets.views import tickets_blueprint
    app.register_blueprint(tickets_blueprint, url_prefix="/tickets")

def create_app():
    """Create app instance."""
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app

    register_blueprints(app)

    return app
