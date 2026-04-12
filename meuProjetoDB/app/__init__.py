from flask import Flask
from app.config import Config
from app.extensions import db, migrate

from app.models.user import User
from app.models.message import Message

from app.controllers.user_controller import user_bp
from app.controllers.message_controller import message_bp
from app.controllers.home_controller import home_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(user_bp, url_prefix="/usuarios")
    app.register_blueprint(message_bp, url_prefix="/mensagens")

    return app