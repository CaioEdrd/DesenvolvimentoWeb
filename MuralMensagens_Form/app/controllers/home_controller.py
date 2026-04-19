from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models.user import User
from app.models.message import Message

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods = ["GET", "POST"])
def home():
    usuarios = User.query.all()
    mensagens = Message.query.all()
    return render_template("pages/index.html", usuarios=usuarios, mensagens = mensagens)