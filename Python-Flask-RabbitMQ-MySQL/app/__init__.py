from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object("config")
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    ma.init_app(app)

    from .models import message  # noqa: F401
    from .routes.routes import api

    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
