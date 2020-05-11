from flask import Flask
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return json.dumps({"message":"hello my flask application!"})

