from flask import Blueprint, render_template, request, redirect, flash
from app.extensions import db
from app.models.message import Message
from app.models.user import User

message_bp = Blueprint("message", __name__)

@message_bp.route("/", methods=["GET", "POST"])
def mensagens():
    usuarios = User.query.all()

    if not usuarios:
        flash("É necessário cadastrar pelo menos um usuário.")
        return redirect("/")

    if request.method == "POST":
        titulo = request.form.get("titulo")
        conteudo = request.form.get("conteudo")
        usuario_id = request.form.get("usuario_id")

        nova_mensagem = Message(
            titulo=titulo,
            conteudo=conteudo,
            usuario_id=usuario_id
        )

        db.session.add(nova_mensagem)
        db.session.commit()

        return redirect("/mensagens")

    mensagens = Message.query.all()

    return render_template(
        "pages/mensagens.html",
        mensagens=mensagens,
        usuarios=usuarios
    )


@message_bp.route("/excluir/<int:id>")
def excluir_mensagem(id):
    mensagem = Message.query.get(id)

    if mensagem:
        db.session.delete(mensagem)
        db.session.commit()

    return redirect("/mensagens")


@message_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_mensagem(id):
    mensagem = Message.query.get(id)
    usuarios = User.query.all()

    if request.method == "POST":
        mensagem.titulo = request.form.get("titulo")
        mensagem.conteudo = request.form.get("conteudo")
        mensagem.usuario_id = request.form.get("usuario_id")

        db.session.commit()

        return redirect("/mensagens")

    return render_template(
        "pages/editar_mensagem.html",
        mensagem=mensagem,
        usuarios=usuarios
    )