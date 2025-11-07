from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify(users=[
        {"id": 1, "name": "Ada"},
        {"id": 2, "name": "Linus"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
