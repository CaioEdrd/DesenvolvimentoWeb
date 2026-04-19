from flask import Flask, render_template
from app.config import Config
from app.extensions import db, migrate

from app.models.projetos import Projeto
from app.models.metas import Meta

from app.controllers.projetos_controller import projeto_bp
from app.controllers.metas_controller import meta_bp
from app.controllers.home_controller import home_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(projeto_bp, url_prefix="/projetos")
    app.register_blueprint(meta_bp, url_prefix="/projetos/<int:projetos_id>")

    @app.route("/")
    def index():
        return render_template("pages/index.html")

    return app