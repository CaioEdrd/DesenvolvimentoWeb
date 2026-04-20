from flask import Blueprint, render_template, redirect, flash, url_for
from app.extensions import db
from app.models.metas import Meta
from app.models.projetos import Projeto
from app.forms.metas_form import MetaForm
from datetime import datetime

meta_bp = Blueprint("metas", __name__)

@meta_bp.route("/metas", methods=["GET", "POST"]) #criação da rota 
def metas(projeto_id): #função principal

    form = MetaForm()

    if form.validate_on_submit():
        nova_meta = Meta(
            descricao=form.descricao.data,
            status=form.status.data,
            projeto_id=projeto_id
        )

        db.session.add(nova_meta)
        db.session.commit()
        flash("Meta criada com sucesso!", "success")

        return redirect(url_for("metas.metas", projeto_id=projeto_id)) #"metas" → nome do blueprint "metas" → nome da função projeto_id → parâmetro da URL
        #return redirect(f"/projetos/{projeto_id}/metas") 

    metas = Meta.query.filter_by(projeto_id=projeto_id).all()
    projeto = Projeto.query.get(projeto_id)    

    return render_template("pages/metas.html", metas=metas, form=form, projeto=projeto)


@meta_bp.route("/metas/excluir/<int:meta_id>")
def excluir_meta(projeto_id,meta_id):
    meta = Meta.query.get(meta_id)

    if meta:
        db.session.delete(meta)
        db.session.commit()
    flash("Meta excluída com sucesso!", "success")

    return redirect(url_for("metas.metas", projeto_id=projeto_id))


@meta_bp.route("/metas/editar/<int:meta_id>", methods=["GET", "POST"])
def editar_meta(projeto_id, meta_id):
    meta = Meta.query.get(meta_id)

    form = MetaForm(obj=meta)

    if form.validate_on_submit():
        meta.descricao=form.descricao.data
        meta.status=form.status.data
        meta.projeto_id=projeto_id

        db.session.commit()
        flash("Meta atualizada com sucesso!", "success")

        return redirect(url_for("metas.metas", projeto_id=projeto_id))
    

    return render_template("pages/editar_meta.html", form=form)

@meta_bp.route("/metas/concluir/<int:meta_id>")
def concluir_meta(projeto_id,meta_id):
    meta = Meta.query.get(meta_id)

    if meta:
        meta.status="Concluída"
        db.session.commit()
    
    flash("Meta concluída com sucesso!", "success")

    return redirect(url_for("metas.metas", projeto_id=projeto_id))

@meta_bp.route("/metas/reabrir/<int:meta_id>")
def reabrir_meta(projeto_id,meta_id):
    meta = Meta.query.get(meta_id)

    if meta:
        meta.status="Pendente"
        db.session.commit()
    
    flash("Meta reaberta com sucesso!", "alert")

    return redirect(url_for("metas.metas", projeto_id=projeto_id))