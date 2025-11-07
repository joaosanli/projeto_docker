import sqlite3, os, time, json
DB_PATH = os.environ.get("DB_PATH", "/data/app.db")

os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT)")
cur.execute("INSERT INTO runs(ts) VALUES (?)", (time.strftime("%Y-%m-%d %H:%M:%S"),))
con.commit()
rows = list(cur.execute("SELECT id, ts FROM runs ORDER BY id"))
print(json.dumps({"db_path": DB_PATH, "rows": rows}, indent=2, ensure_ascii=False))
con.close()
