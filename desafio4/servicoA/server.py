from flask import Flask, jsonify
app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Ada Lovelace"},
    {"id": 2, "name": "Alan Turing"},
    {"id": 3, "name": "Grace Hopper"},
]

@app.route("/users")
def users():
    return jsonify(users=USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
