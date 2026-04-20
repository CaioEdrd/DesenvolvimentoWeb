from flask_wtf import FlaskForm #biblioteca para montar o form
from wtforms import TextAreaField, SelectField #biblioteca para os tipos de campos
from wtforms.validators import DataRequired #biblioteca para validar

class MetaForm(FlaskForm): #criação do formulário
    descricao = TextAreaField("Descrição", validators=[DataRequired()]) #campo descrição do tipo campo área de texto, nome "Titulo" e obrigatório
    status = SelectField("Status", choices=[("Pendente","Pendente"),("Concluída","Concluída")])
