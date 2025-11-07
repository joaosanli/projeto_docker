from flask import Flask, jsonify
import os, requests

A_URL = os.environ.get("A_URL", "http://servicoA:5000")
app = Flask(__name__)

@app.route("/report")
def report():
    try:
        r = requests.get(f"{A_URL}/users", timeout=5)
        r.raise_for_status()
        users = r.json().get("users", [])
        lines = [f"Usuário {u['id']}: {u['name']} — ativo desde 2020"]
        return jsonify(report=lines, total=len(users))
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
