# src/app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    api_key = os.getenv("API_KEY", "No API Key Found")
    return f"<h2>Secure CI/CD Demo App</h2><p>API Key: {api_key}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)