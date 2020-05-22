from flask import Blueprint, render_template, abort
from ext.database import Aluno

bp = Blueprint("webui", __name__, template_folder='templates')

@bp.route('/')
def estudantes():
    estudantes = Aluno.query.all()
    return render_template('index.html', estudantes=estudantes)

def init_app(app):
    app.register_blueprint(bp)