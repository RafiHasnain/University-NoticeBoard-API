from flask import Flask, jsonify
import json
import subprocess

app = Flask(__name__)

with open('sample.json') as f:
    data = json.load(f)


@app.route('/', methods=['GET'])
def index():
    subprocess.run('python3 web.py', shell=True)
    return jsonify(data)
