from flask import Blueprint, render_template, redirect, flash
from app.extensions import db
from app.models.message import Message
from app.models.user import User
from app.forms.message_form import MessageForm

message_bp = Blueprint("message", __name__)

@message_bp.route("/", methods=["GET", "POST"])
def mensagens():
    usuarios = User.query.all()

    if not usuarios:
        flash("É necessário cadastrar pelo menos um usuário.")
        return redirect("/")

    form = MessageForm()
    form.usuario_id.choices = [(u.id, u.nome) for u in usuarios]

    if form.validate_on_submit():
        nova_mensagem = Message(
            titulo=form.titulo.data,
            conteudo=form.conteudo.data,
            usuario_id=form.usuario_id.data
        )

        db.session.add(nova_mensagem)
        db.session.commit()

        return redirect("/mensagens")

    mensagens = Message.query.all()

    return render_template("pages/mensagens.html", mensagens=mensagens, form=form)


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

    form = MessageForm(obj=mensagem)
    form.usuario_id.choices = [(u.id, u.nome) for u in usuarios]

    if form.validate_on_submit():
        mensagem.titulo = form.titulo.data
        mensagem.conteudo = form.conteudo.data
        mensagem.usuario_id = form.usuario_id.data

        db.session.commit()
        return redirect("/mensagens")

    return render_template("pages/editar_mensagem.html", form=form)