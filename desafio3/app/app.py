from flask import Flask, jsonify
import os, time
import psycopg2
import redis

app = Flask(__name__)

PG_DSN = {
    "host": os.environ.get("POSTGRES_HOST", "db"),
    "port": int(os.environ.get("POSTGRES_PORT", "5432")),
    "dbname": os.environ.get("POSTGRES_DB", "appdb"),
    "user": os.environ.get("POSTGRES_USER", "app"),
    "password": os.environ.get("POSTGRES_PASSWORD", "secret"),
}
REDIS_HOST = os.environ.get("REDIS_HOST", "cache")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

def wait_for_postgres():
    for i in range(30):
        try:
            con = psycopg2.connect(**PG_DSN)
            con.close()
            return
        except Exception as e:
            time.sleep(1)
    raise RuntimeError("Postgres não respondeu a tempo.")

def init_db():
    con = psycopg2.connect(**PG_DSN)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users(name) VALUES ('Ada'), ('Linus') ON CONFLICT DO NOTHING;")
    con.commit()
    cur.close()
    con.close()

def get_users():
    con = psycopg2.connect(**PG_DSN)
    cur = con.cursor()
    cur.execute("SELECT id, name FROM users ORDER BY id")
    data = [{"id": r[0], "name": r[1]} for r in cur.fetchall()]
    cur.close()
    con.close()
    return data

def get_redis():
    for _ in range(30):
        try:
            r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
            r.ping()
            return r
        except Exception:
            time.sleep(1)
    raise RuntimeError("Redis não respondeu a tempo.")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/hit")
def hit():
    r = get_redis()
    val = r.incr("hits")
    return jsonify(hits=val)

@app.route("/users")
def users():
    return jsonify(users=get_users())

if __name__ == "__main__":
    wait_for_postgres()
    init_db()
    app.run(host="0.0.0.0", port=5000)
