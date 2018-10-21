from flask import Flask
from flask import request
from healthcare import readDataForHealthcare
from score_calculation import *
import json

import os, sys

app = Flask(__name__)

@app.route('/start')
def index():
	return "Hello World!"

#@app.route('/json', methods = ['GET'])
#def jsonObj():
#    obj = readDataForHealthcare("test.csv")
#    return obj

@app.route('/whereToGo', methods = ['GET'])
def whereToGo():
    obj = score_calculation("6.5244,3.3792")
    return obj

@app.route('/whereToCamp', methods = ['GET'])
def whereToCamp():
    with open("./resources/vegetation_means.json") as f:
        data = json.load(f)
    return json.dumps(data)