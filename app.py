#Extensões nativas do Flask
from flask import Flask, jsonify, request
#Extensões externas
from flask_sqlalchemy import SQLAlchemy
from dynaconf import FlaskDynaconf

import requests, os, click

app = Flask(__name__)
FlaskDynaconf(app)

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable = False)
    gender = db.Column(db.String(1))
    address = db.Column(db.String(200), nullable = False)

#Adicionando um novo comando à interface do Flask
@app.cli.command()
def create_database():
    """Executa a criação das tabelas registradas na ORM."""
    db.create_all()

@app.route('/')
def index():
    return jsonify({"message":"My json!"})

@app.route('/cursos/', methods=['GET', 'POST'])
def cursos():

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"userId":"1", "title": "Coding test API", "body": "Testando a API do jsonplaceholder."}

    if request.method == 'GET':       
        
        return jsonify([{"nome":"ECP Quarentena","tipo":"EAD"},
                        {"nome":"Inteligencia Artificial", "tipo":"Presencial"},
                        {"nome":"Alura Cursos", "tipo":"EAD"}])
    
    if request.method == 'POST':
        
        request_ = requests.post(url, data=data)
    
        return request_.content, request_.status_code
    