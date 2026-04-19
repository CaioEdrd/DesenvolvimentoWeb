from flask import Blueprint, render_template, redirect, flash
from app.extensions import db
from app.models.user import User
from app.forms.user_form import UserForm

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET", "POST"])
def usuarios():
    form = UserForm()

    if form.validate_on_submit():
        usuario_existente = User.query.filter_by(email=form.email.data).first()

        if usuario_existente:
            flash("Já existe um usuário com esse email.")
            return redirect("/usuarios")

        novo_usuario = User(
            nome=form.nome.data,
            email=form.email.data
        )

        db.session.add(novo_usuario)
        db.session.commit()

        return redirect("/usuarios")

    usuarios = User.query.all()

    return render_template("pages/usuarios.html", usuarios=usuarios, form=form)