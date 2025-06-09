from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20,)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha', message='As senhas devem coincidir.')])
    botao_submit_criar_conta = SubmitField('Criar Conta')

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20, )])
    botao_submit_login = SubmitField('Fazer Login')