from app.extensions import db #importa o módulo do banco que foi instanciado nas extensões
from datetime import datetime

class Projeto(db.Model): #cria a tabela "Projeto"
    id = db.Column(db.Integer, primary_key=True) #cria a coluna de id sendo "int" e chave primária 
    nome = db.Column(db.String(150), nullable=False) #cria a coluna do nome do projeto sendo string e não nula
    descricao = db.Column(db.Text, nullable=False) #cria a coluna do descrição do projeto sendo text e não nulo
    data_criacao = db.Column(db.DateTime, default=datetime.now) #utiliza da biblioteca date time para puxar a data e hora de criação
    data_edicao = db.Column(db.DateTime, onupdate=datetime.now)

    metas = db.relationship("Meta", backref="projeto", lazy=True, cascade="all, delete-orphan")