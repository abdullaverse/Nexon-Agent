from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    time.sleep(2)  # slow server
    return "⚡ Server B Response"

app.run(port=5002)