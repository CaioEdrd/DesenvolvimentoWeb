from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired()])
    conteudo = TextAreaField("Conteúdo", validators=[DataRequired()])
    usuario_id = SelectField("Usuário", coerce=int)