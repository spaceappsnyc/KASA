from flask import Flask
from flask import request

import os, sys

app = Flask(__name__)

@app.route('/start')
def index():
	return "Hello World!"
