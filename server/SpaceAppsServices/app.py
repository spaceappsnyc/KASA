from flask import Flask
from flask import request
from score_calculation import *
import json

import os, sys

app = Flask(__name__)

@app.route('/start')
def index():
	return "Hello World!"

@app.route('/whereToGo', methods = ['GET'])
def whereToGo():
    with open("./resources/score_list.json") as f:
        data = json.load(f)
    return json.dumps(data)

@app.route('/whereToCamp', methods = ['GET'])
def whereToCamp():
    with open("./resources/vegetation_means.json") as f:
        data = json.load(f)
    return json.dumps(data)