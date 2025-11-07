from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/users")
def users():
    r = requests.get("http://users:5000/users", timeout=5)
    return jsonify(r.json())

@app.route("/orders")
def orders():
    r = requests.get("http://orders:5000/orders", timeout=5)
    return jsonify(r.json())

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
