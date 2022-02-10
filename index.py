import requests
from flask import Flask, request
import json

app = Flask(__name__)
url = "http://dougserver:8000/relay"
plcUrl = "http://192.168.43.38/?r"

@app.route('/arduino/<relay>/<state>')
def arduino(relay, state):
    req = requests.get(plcUrl + relay + state)
    return 'Relay 1'

@app.route("/")
def home():
    return "py home.."

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