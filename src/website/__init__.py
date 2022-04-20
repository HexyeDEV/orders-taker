from flask import Flask, flash, request
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'secret by hexye and orders btw kim isnt so ban and orders taker is revolutionary and geniusly bad'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views)
    app.register_blueprint(auth, url_prefix="/auth")

    from .models import Room, Order
    create_db(app)
    
    return app

def create_db(app):
    if not path.exists("database.db"):
        db.create_all(app=app)