from flask import render_template, Blueprint, redirect, request
from ext.database import Aluno, db, save_to

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, validators
import email_validator

bp = Blueprint("cadastro", __name__, template_folder='templates')

class FormularioEstudante(FlaskForm):
    nome = StringField('Nome', 
                        validators=[validators.DataRequired(message='Por favor complete com os dados corretamente.')])
    email = StringField('Email', 
                        validators=[validators.DataRequired(message='Por favor complete com os dados corretamente.'), validators.Email(message='Este não é um email válido')])
    genero = SelectField(u'Gênero',choices=[('m','M'),('f','F')])
    endereco = StringField('Endereço', validators=[validators.DataRequired()])
    submit = SubmitField('Enviar')

@bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    
    form = FormularioEstudante(request.form)
    
    if form.validate_on_submit():
        aluno = form.data.copy()
        data = Aluno(aluno)
        save_to(data, db)

        return redirect('/')
    
    return render_template('cadastro.html', form=form)

def init_app(app):
    app.register_blueprint(bp)

