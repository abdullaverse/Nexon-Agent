from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    time.sleep(0.5)  # fast server
    return "🚀 Server A Response"

app.run(port=5001)