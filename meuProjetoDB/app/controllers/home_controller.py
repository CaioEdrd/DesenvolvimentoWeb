from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models import user, message

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods = ["GET", "POST"])
def home():
    usuarios = user.User.query.all()
    mensagens = message.Message.query.all()
    return render_template("pages/index.html", usuarios=usuarios, mensagens = mensagens)