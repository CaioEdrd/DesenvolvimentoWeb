from flask import Blueprint, render_template, redirect, flash
from app.extensions import db
from app.models.metas import Meta
from app.models.projetos import Projeto
from app.forms.metas_form import MetaForm

meta_bp = Blueprint("metas", __name__)

@meta_bp.route("/", methods=["GET", "POST"]) #criação da rota 
def metas(): #função principal

    form = MetaForm()

    if form.validate_on_submit():
        nova_meta = Meta(
            descricao=form.descricao.data,
            status=form.status.data,
            projeto_id=form.projeto_id.data
        )

        db.session.add(nova_meta)
        db.session.commit()

        return redirect("/")

    metas = Meta.query.all()

    return render_template("pages/metas.html", metas=metas, form=form)


@meta_bp.route("metas/excluir/<int:meta_id>")
def excluir_meta(meta_id):
    meta = Meta.query.get(meta_id)

    if meta:
        db.session.delete(meta)
        db.session.commit()

    return redirect("/")


@meta_bp.route("/metas/editar/<int:meta_id>", methods=["GET", "POST"])
def editar_mensagem(meta_id):
    meta = Meta.query.get(meta_id)

    form = MetaForm(obj=meta)

    if form.validate_on_submit():
        meta.descricao=form.descricao.data,
        meta.status=form.status.data,
        meta.projeto_id=form.projeto_id.data

        db.session.commit()
        return redirect("/")

    return render_template("pages/editar_meta.html", form=form)