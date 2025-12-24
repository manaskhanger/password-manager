from crypto import encrypt, decrypt


def add_entry(conn, key, service, username, password):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vault (service, username, password) VALUES (?, ?, ?)",
        (service, encrypt(username, key), encrypt(password, key))
    )
    conn.commit()


def fetch_entries(conn, key):
    cursor = conn.cursor()
    cursor.execute("SELECT service, username, password FROM vault")
    rows = cursor.fetchall()

    entries = []
    for service, username, password in rows:
        entries.append((
            service,
            decrypt(username, key),
            decrypt(password, key)
        ))
    return entries
