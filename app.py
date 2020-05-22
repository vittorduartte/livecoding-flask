#Extensões nativas do Flask
from flask import Flask, jsonify, request
#Extensões externas
from flask_sqlalchemy import SQLAlchemy
from dynaconf import FlaskDynaconf
#Outras extensões
import requests, os, click
#Factory's
from ext import database
from ext import configuration
from ext import commands
from ext import bootstrap
import blueprints.webui as webui
from blueprints.webui import form

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
commands.init_app(app)
webui.init_app(app)
bootstrap.init_app(app)
form.init_app(app)

    