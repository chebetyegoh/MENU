"""
Configuration file for the flask app.
"""

from os import environ

from dotenv import load_dotenv

# load environment variables
load_dotenv()


class DevelopmentConfig(object):
    """Configuration during development"""
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(object):
    ...


class ProductionConfig(object):
    ...


APP_CONFIG = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
