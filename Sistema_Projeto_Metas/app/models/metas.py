from app.extensions import db #importa o módulo do banco que foi instanciado nas extensões
from datetime import datetime

class Meta(db.Model): #cria a tabela "Meta"
    id = db.Column(db.Integer, primary_key=True) #cria a coluna de id sendo "int" e chave primária 
    descricao = db.Column(db.Text, nullable=False) #cria a coluna do descrição do projeto sendo text e não nulo
    status = db.Column(db.Text, nullable=False) #cria a coluna de status como bool
    data_criacao = db.Column(db.DateTime, default=datetime.now) #utiliza da biblioteca date time para puxar a data e hora de criação
    data_edicao = db.Column(db.DateTime, onupdate=datetime.now)
    
    projeto_id = db.Column(db.Integer, db.ForeignKey("projeto.id", ondelete="CASCADE"))