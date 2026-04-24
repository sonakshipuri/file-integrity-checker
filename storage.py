import json
import os

DB = "hashes.json"

def load_db():
    if not os.path.exists(DB):
        return {}

    if os.path.getsize(DB) == 0:
        return {}

    try:
        with open(DB, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_db(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=2)

def store_record(path, algo, value):
    db = load_db()
    db[path] = {
        "algo": algo,
        "hash": value
    }
    save_db(db)

def get_record(path):
    db = load_db()
    return db.get(path)