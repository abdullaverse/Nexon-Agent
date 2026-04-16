from monitor import get_latency

servers = {
    "Server A": "https://example.com",
    "Server B": "https://google.com"
}

history = {"Server A": [], "Server B": []}


# 🔮 AI Prediction (trend-based)
def predict_failure(latency_list):
    if len(latency_list) < 3:
        return False
    return latency_list[-1] > latency_list[-2] > latency_list[-3]


# 📊 Confidence score
def confidence_score(latency):
    if latency < 1:
        return 95
    elif latency < 2:
        return 75
    else:
        return 40


def get_best_server():
    latencies = {}
    predictions = {}
    scores = {}

    for name, url in servers.items():
        latency = get_latency(url)
        history[name].append(latency)

        if len(history[name]) > 5:
            history[name].pop(0)

        avg_latency = sum(history[name]) / len(history[name])
        latencies[name] = avg_latency

        # AI features
        predictions[name] = predict_failure(history[name])
        scores[name] = confidence_score(avg_latency)

    best = min(latencies, key=latencies.get)

    return servers[best], best, latencies, predictions, scores,history