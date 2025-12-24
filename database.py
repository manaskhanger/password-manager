import sqlite3

def init_db():
    conn = sqlite3.connect("vault.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        salt BLOB,
        password_hash BLOB
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS vault (
        id INTEGER PRIMARY KEY,
        service TEXT,
        username BLOB,
        password BLOB
    )""")
    conn.commit()
    conn.close()
