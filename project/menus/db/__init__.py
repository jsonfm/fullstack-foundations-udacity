from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from menus.config import config

# create the extension
database = SQLAlchemy()


def configure_database(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = config["DB_URL"]
    database.init_app(app)
    return database
