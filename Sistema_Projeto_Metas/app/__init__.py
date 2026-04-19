from flask import Flask, render_template
from app.config import Config
from app.extensions import db, migrate

from app.models.projetos import User
from app.models.metas import Message

from app.controllers.projetos_controller import projetos_bp
from app.controllers.metas_controller import metas_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp, url_prefix="/usuarios")
    app.register_blueprint(message_bp, url_prefix="/mensagens")

    @app.route("/")
    def index():
        return render_template("pages/index.html")

    return app