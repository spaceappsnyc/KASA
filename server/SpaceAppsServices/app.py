from flask import Flask
from flask import request
from score_calculation import *

import os, sys

app = Flask(__name__)

@app.route('/start')
def index():
	return "Hello World!"

@app.route('/whereToGo', methods = ['GET'])
def whereToGo():
    obj = score_calculation("7.247324,6.010124")
    return obj
