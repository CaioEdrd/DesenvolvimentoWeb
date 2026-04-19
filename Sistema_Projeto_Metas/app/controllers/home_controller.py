from flask import Blueprint, render_template, redirect
from app.extensions import db
from app.models.projetos import Projeto

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods = ["GET", "POST"])
def home():
    projetos = Projeto.query.all()
    return render_template("pages/index.html", projetos=projetos)