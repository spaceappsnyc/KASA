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
    obj = score_calculation("7.247324,6.010124")
    return obj

@app.route('/whereToCamp', methods = ['GET'])
def whereToCamp():
    with open("./resources/vegetation_means.json") as f:
        data = json.load(f)
    return json.dumps(data)