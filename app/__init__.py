from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from config import Config
def build_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from . import models
    from . import routes
    app.register_blueprint(routes.main)
    return app