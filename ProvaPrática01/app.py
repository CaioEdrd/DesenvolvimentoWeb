from flask import Flask, render_template, request, redirect, flash
import os, datetime

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

usuarios=[]
mensagens=[]
qtdUsuarios = len(usuarios)
qtdMensagens = len(mensagens)

@app.route("/", methods=["GET","POST"])
def home():

    return render_template("pages/index.html", qtdMensagens=qtdMensagens, qtdUsuarios=qtdUsuarios, mensagens=mensagens, usuarios=usuarios)

@app.route("/usuarios", methods=["GET","POST"])
def cadastrar():
    if request.method == "POST":
        usuario = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email")
        }

        if usuario["email"]:
            for u in usuarios:
                if u["email"] == usuario["email"]:
                    flash("E-mail já cadastrado!", "danger")
                    break
            else:
                usuarios.append(usuario)
                flash("Cadastro realizado com sucesso!", "success")
                

        return redirect("/")
    return render_template("pages/usuarios.html", usuarios=usuarios, qtdUsuarios=qtdUsuarios, mensagens=mensagens)

@app.route("/mensagens", methods=["GET","POST"])
def mensagem():
    if request.method == "POST":
        usuario_email = request.form.get("usuario_email")

        contador = 0

        for m in mensagens:
            if m["usuario_email"] == usuario_email:
                contador += 1

        mensagem={
            'titulo':request.form.get("titulo"),
            'conteudo':request.form.get("conteudo"),
            'data_hora':datetime.datetime.now(),
            'usuario_email':usuario_email,
            'qtd_mensagens':contador + 1
        }

        mensagens.append(mensagem)
        
        mensagens.sort(key=lambda m: m["data_hora"], reverse=True)

        return redirect("/")
    return render_template("pages/mensagens.html", usuarios=usuarios, mensagens=mensagens, qtdMensagens=qtdMensagens)