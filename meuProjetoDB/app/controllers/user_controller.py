from flask import Blueprint, render_template, request, redirect
from app.extensions import db
from app.models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET", "POST"])
def usuarios():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        novo_usuario = User(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect("/usuarios")

    usuarios = User.query.all()
    return render_template("pages/usuarios.html", usuarios=usuarios)