from flask import Flask, request

from modules.create_user import create_user

app = Flask(__name__)

def response(input):
    if input: return input, 200
    return "", 200

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/api/create_user", methods=["POST"])
def run_create_user(): 
    return response(create_user(request))