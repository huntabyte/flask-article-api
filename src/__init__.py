from flask import Flask
from src.extensions import db, ma


def create_app(script_info=None):

    app = Flask(__name__)
    app.config.from_object("src.config.DevelopmentConfig")

    register_extensions(app)

    from src.api import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
