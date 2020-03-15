from flask import Flask

from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

@app.route("/geo/data.json")
def return_dataasdf():
    with open("data/data_alt.json",'r') as f:
        v = f.read()
    
    return v #json.loads(f)

@app.route("/geo/greek_graph.json")
def return_data():
    with open("data/greek_graph.json",'r') as f:
        v = f.read()
    
    return v #json.loads(f)

@app.route("/geo/greece.json")
def return_greece():
    with open("greece_geo.json",'r') as f:
        v = f.read()
    
    return v #json.loads(f)
