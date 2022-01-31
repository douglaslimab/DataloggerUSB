import requests
from flask import Flask, request
import json

app = Flask(__name__)
url = "http://dougserver:8000/relay"

@app.route("/")
def home():
    return "this is home.."

@app.route("/relay")
def relay():
    return "relay status!!"

@app.route(("/on/relay=<address>"))
def turnOn(address):
    req = requests.get(url + "/" + address)
    out = req.json()
    return out

@app.route(("/off/relay=<address>"))
def turnOff(address):
    req = requests.get(url + "/" + address)
    return req.json()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')