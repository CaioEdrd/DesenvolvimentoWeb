import os
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form.get("nome")

        if nome:
            flash("Mensagem enviada com sucesso!", "success")
        else:
            flash("Erro: o nome é obrigatório.", "danger")

        return redirect("/")

    return render_template("pages/index.html")