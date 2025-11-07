from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
START = time.time()
COUNTER = 0

@app.route('/')
def index():
    global COUNTER
    COUNTER += 1
    return jsonify({
        "service": "d1-server",
        "counter": COUNTER,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "env": dict(os.environ)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
