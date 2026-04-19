from flask import Blueprint, render_template, redirect, flash
from app.extensions import db
from app.models.projetos import Projeto
from app.forms.projetos_form import ProjetoForm

projeto_bp = Blueprint("projetos", __name__)

@projeto_bp.route("/", methods=["GET", "POST"]) #criação da rota 
def projetos(): #função principal
    projetos = Projeto.query.all() #select na tabela Projeto

    form = ProjetoForm() #inicialização do formulário

    if form.validate_on_submit(): #verifica se o formulário está com os campos valdiados
        novo_projeto = Projeto( #criação do item
            nome=form.nome.data,
            descricao=form.descricao.data,
        )

        db.session.add(novo_projeto) #adição na tabela
        db.session.commit() #salva a transação no banco

        return redirect("/")


    return render_template("pages/projetos.html", form=form, projetos=projetos)


@projeto_bp.route("/excluir/<int:id>")
def excluir_projeto(id):
    projeto = Projeto.query.get(id)

    if projeto:
        db.session.delete(projeto)
        db.session.commit()

    return redirect("/projetos")


@projeto_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_projeto(id):
    projeto = Projeto.query.get(id)

    form = ProjetoForm(obj=projeto)

    if form.validate_on_submit():
        projeto.nome=form.nome.data
        projeto.descricao=form.descricao.data

        db.session.commit()
        return redirect("/projetos")

    return render_template("pages/editar_projeto.html", form=form)