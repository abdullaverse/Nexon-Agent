from flask import Flask, redirect
from dns_logic import get_best_server

app = Flask(__name__)

@app.route('/')
def route():
    best_url, best_name, data, predictions, scores = get_best_server()

    # 🧠 Self-healing simulation
    if data[best_name] > 3:
        print("⚠️ High latency detected - triggering recovery")

    return redirect(best_url)

app.run(port=5000)