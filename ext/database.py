from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Aluno(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    nome = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    genero = db.Column(db.String(1))
    endereco = db.Column(db.String(200), nullable = False)

    def __init__(self, dict):
        self.__dict__.update(dict)

def save_to(data, db):
    db.session.add(data)
    db.session.commit()

def init_app(app):
    db.init_app(app)