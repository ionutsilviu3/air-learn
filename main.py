from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
app.debug = True
@app.route("/")
def index():
    return "<h1>vai de viata noastra</h1>"

app.run('localhost', port=8080)