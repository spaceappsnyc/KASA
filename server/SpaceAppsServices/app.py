from flask import Flask
from flask import request
from healthcare import readDataForHealthcare

import os, sys

app = Flask(__name__)

@app.route('/start')
def index():
	return "Hello World!"

@app.route('/json', methods = ['GET'])
def jsonObj():
    obj = readDataForHealthcare("test.csv")
    return obj
