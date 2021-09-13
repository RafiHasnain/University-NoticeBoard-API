from flask import Flask, jsonify
import json
import subprocess

app = Flask(__name__)

with open('notices.json') as f:
    data = json.load(f)


@app.route('/', methods=['GET'])
async def index():
    subprocess.run('python3 web.py', shell=True)
    return jsonify(data)
