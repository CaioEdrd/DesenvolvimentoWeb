from flask_wtf import FlaskForm #biblioteca para montar o form
from wtforms import TextAreaField, StringField #biblioteca para os tipos de campos
from wtforms.validators import DataRequired #biblioteca para validar

class ProjetoForm(FlaskForm): #criação do formulário
    nome = StringField("Nome", validators=[DataRequired()]) #campo nome do tipo área de texto, nome "Nome" e obrigatório
    descricao = TextAreaField("Descrição", validators=[DataRequired()]) #campo descrição do tipo campo área de texto, nome "Descrição" e obrigatório
