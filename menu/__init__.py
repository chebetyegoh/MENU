from flask import Flask
from flask_migrate import Migrate
from menu.config.config import APP_CONFIG
from menu.db.database import db
from menu.home.views import home as homeViews
from menu.Auth.views import auth as authViews
from menu.login.login import login_manager


def create_app():
    """Actual app creation"""
    app = Flask(__name__)
    app.config.from_object(APP_CONFIG["development"])
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    # Register blueprint apps
    app.register_blueprint(homeViews)
    app.register_blueprint(authViews)

    return app
