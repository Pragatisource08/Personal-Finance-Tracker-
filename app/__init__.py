from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from config import Config
def build_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from . import routes
    from . import models
    return app