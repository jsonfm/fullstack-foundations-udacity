from flask import Flask
from menus.config import config
from menus.db import database as db


def create_app():
    app = Flask(__name__)
    DB_URL = config.get('DB_URL', "sqlite:///menus.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app