import requests
import time

def get_latency(url):
    try:
        start = time.time()
        requests.get(url, timeout=2)
        return round(time.time() - start, 3)
    except:
        return float('inf')