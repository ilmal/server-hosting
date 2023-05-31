from flask import Flask, request

from modules.create_user import create_user
from modules.create_server import create_server

app = Flask(__name__)

def response(input):
    if input: return input, 200
    return "", 200

@app.route("/api/")
def hello_world():
    return "Hello world"

@app.route("/api/create_user", methods=["POST"])
def run_create_user(): 
    return response(create_user(request))

@app.route("/api/create_server", methods=["POST"])
def run_create_server():
    return response(create_server(request))